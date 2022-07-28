var taskList = document.getElementById("tasklist");
var reorderForm = document.getElementById("reorderForm");
var positionInput = document.getElementById("positionInput");

let sortable = Sortable.create(taskList, {
	handle: '.handle',
	ghostClass: 'dropArea',
	chosenClass: 'selectedTask',

});

function reordering() {
	const rows = document.getElementsByClassName("task-wrapper");
	let pos = [];
	for (let row of rows) {
		pos.push(row.dataset.position);
	}
	positionInput.value = pos.join(',');
	reorderForm.submit();
}

document.ondrop = reordering

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');




function complete_toggle(eid){
	// console.log(eid);
	if ($("#"+eid).attr('class') =="task-incomplete-icon") {
		$.ajax({
				url: 'api/'+eid+'/',
				headers: {
					"X-CSRFToken": csrftoken
				   },
				method: 'PATCH',
				contentType : 'application/json',
				data: JSON.stringify({"complete":true}),
				success: function(data){
				$("#"+eid).attr('class', "task-complete-icon");
				}
				});
		} 
		
		else {
			$.ajax({
				url: 'api/'+eid+'/',
				headers: {
					"X-CSRFToken": csrftoken
				   },
				method: 'PATCH',
				contentType : 'application/json',
				data: JSON.stringify({"complete":false}),
				success: function(data){
				$("#"+eid).attr('class', "task-incomplete-icon");
				}
				});
		}
	}