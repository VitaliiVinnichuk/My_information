$(document).ready(function () {
    setInterval(function () {
        requestUpdate();
    }, 5000)
});


var req_counter = 0;
var isActive = false;
var default_title = document.title;


//Browser tab in focus
$(window).focus(function () {
    req_counter = 0;
    document.title = default_title;
    isActive = true;
});

$(window).blur(function () {
    isActive = false;
});


//title new request counter
function titleCounter(last_id) {
    var tmp = 0;
    if (prev_id == 0) {
        prev_id = last_id;
        tmp = prev_id;
    }else{
        tmp = prev_id;
        prev_id = last_id;}
    if (last_id - tmp == 0)
        return;
    var x = last_id - tmp;
    req_counter += x;
    if (req_counter > 0 && !isActive)
        document.title = "(" + req_counter + ") " + default_title;
}

function requestUpdate(callback) {
    $.ajax({
        dataType: "json",
        url: '/request_logger/',
        success: function (response) {
            var last_id = updateTable(response);
            titleCounter(last_id);
        }
    })
}

function updateTable(data) {
    var newTable = "";
    var response_data = data;
    var date = new Date();
    for (var i = 0; i < response_data.length; i++) {
        date = new Date(response_data[i]["fields"]["time"]);
        newTable +=
            "<tr>" +
            "<td>" + moment(date).format('MMMM D, YYYY, h:mm a') + "</td>" +
            "<td>" + response_data[i]["fields"]["request_method"] + "</td>" +
            "<td>" + response_data[i]["fields"]["ip_addr"] + "</td>" +
            "<td>" + response_data[i]["fields"]["full_path"] + "</td>" +
            "<td>" + "1" + "</td>" +
            "</tr>";
    }
    document.getElementById('requests_table').innerHTML = newTable;
    return response_data[0]["pk"];
}
