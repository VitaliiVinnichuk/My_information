document.getElementById('id_photo').addEventListener('change', function (event) {
    var output = document.getElementById('output_photo');
    output.src = URL.createObjectURL(event.target.files[0]);
}, true);