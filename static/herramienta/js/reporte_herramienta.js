function ListaEdiciones(id) {
    $.ajax({
        url:'/herramientas/reporte/'+id,
        type: 'GET',
        dataType: 'json',
        success: function(response){
            var data = response.lista_ediciones;
            var modal = $("#tabla_ediciones tbody");
            var html;
            data.forEach(function (element) {
                html +=`<tr>
                    <td>${element.usuarioHerramienta__username}</td>
                    <td>${element.creacion}</td>
                </tr>`;
            });
            modal.html("");
            modal.append(html);
            $('#myModal').modal('show')
        }
    })
}

function ListaTutorial(id) {
$.ajax({
        url:'/herramientas/reporte/tutoriales/'+id,
        type: 'GET',
        dataType: 'json',
        success: function(response){
            var data = response.lista_tutoriales;
            var modal = $("#tabla_tutoriales tbody");
            var html;
            data.forEach(function (element) {
                html +=`<tr>
                    <td ><a href="#" onclick="openDetailTutorial(${element.id})"> ${element.nombre} </a></td>
                </tr>`;
            });
            modal.html("");
            modal.append(html);
            $('#myModal2').modal('show')
        }
    })
}

function ListaEjemplos(id) {
    $.ajax({
        url:'/herramientas/reporte/ejemplos/'+id,
        type: 'GET',
        dataType: 'json',
        success: function(response){
            var data = response.lista_ejemplos;
            var modal1 = $("#tabla_ejemplos tbody");
            var html1;
            data.forEach(function (element) {
                html1 +=`<tr>
                    <td><a href="/herramientas/ejemplo/${element.id}">${element.nombre}</a></td>
                </tr>`;
            });
            modal1.html("");
            modal1.append(html1);
            $('#myModal1').modal('show')
        }
    })

}
function  openDetailTutorial(id) {
    window.location='/herramientas/reporte/tutoriales/detail/'+id
}