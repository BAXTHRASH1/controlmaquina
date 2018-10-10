function buscar(){
	keyUsuario = $('#keyUsuario').val()
	if (keyUsuario != '') {
		$.ajax({
			type:'POST',
        	url:'/estadomaquina/',
        	dataType:'json',
        	data:{'csrfmiddlewaretoken':csrftoken,'keyUsuario':keyUsuario},
        	success:function(mydata){
        		modeloMaquina = mydata[0].modeloMaquina
        		estadoPanel = mydata[0].estadoPanel
        		estadoNavegador = mydata[0].estadoNavegador
        		estadoNucleo = mydata[0].estadoNucleo
        		$('#keyUsuario').val('')
        		if (modeloMaquina == 'error') {
        			alert('ERROR DE CONEXION!!')
        		}
        		else{
	        		$('#modeloMaquina').html(modeloMaquina)
	        		$('#busqueda').html(
	        		"Key Actual:<input type='text' id='keyBusqueda' class='form-control' readonly>"+
					"<input type='text' id='comandoSocket' class='form-control' placeholder='codigo de busqueda'><br>"+
					"<input type='button' class='btn btn-dark' value='Buscar' onclick='buscarSocket();'>"+
					"<input type='button' class='btn btn-dark' value='Limpiar' onclick='limpiar();'>"
	        		)
	        		$('#keyBusqueda').val(keyUsuario)
	        		$('#mensajeSocket').html('')
	        		$('#estadoEscritorio').html('').removeClass()
	        		$('#estadoNavegador').html('').removeClass()
	        		$('#estadoPrograma').html('').removeClass()
	        		if (estadoPanel == 'error') {
	        			$('#estadoEscritorio').html('no').addClass('badge badge-pill badge-danger')
	        		}else{
	        			$('#estadoEscritorio').html('ok').addClass('badge badge-pill badge-success')
	        		}
	        		if (estadoNavegador == 'error' ) {
	        			$('#estadoNavegador').html('no').addClass('badge badge-pill badge-danger')
	        		}else{
	        			$('#estadoNavegador').html('ok').addClass('badge badge-pill badge-success')
	        		}
	        		if (estadoNucleo == 'error') {
	        			$('#estadoPrograma').html('no').addClass('badge badge-pill badge-danger')
	        		}else {
	        			$('#estadoPrograma').html('ok').addClass('badge badge-pill badge-success')
	        		}
	        		$('#botonesReinicio').html(
        			"<input type='button'  class='btn btn-dark' value='Reiniciar Escritorio'><br>"+
        			"<input type='button'  class='btn btn-dark' value='Reiniciar Navegador' onclick='reinicioNavegador();'><br>"+
        			"<input type='button'  class='btn btn-dark' value='Reiniciar Sistema' ><br>"+
        			"<input type='button'  class='btn btn-danger' value='Reiniciar Maquina'><br>"
        			)
        		}
        	}
		})
	}
}

function buscarSocket(){
	comandoSocket = $('#comandoSocket').val()
	keyBusqueda = $('#keyBusqueda').val()
	if (comandoSocket != '') {
		$.ajax({
			type:'POST',
        	url:'/buscarsocket/',
        	dataType:'json',
        	data:{'csrfmiddlewaretoken':csrftoken,'comandoSocket':comandoSocket,'keyBusqueda':keyBusqueda},
        	success:function(mydata){
        		msjSocket = mydata[0].mensajeSocket
        		if (msjSocket =='error') {
        			$('#mensajeSocket').prepend('<tr><th>¡error!</th></tr>').css('color','black')
        		}
        		else{
        			$('#mensajeSocket').prepend('<tr><th>'+msjSocket+'</th></tr>').css('color','black')
        		}
        	
        	}
		})
	}
	else {
		alert('INGRESE UNA KEY')
	}
}

function limpiar(){
	$('#mensajeSocket').html('')
}

