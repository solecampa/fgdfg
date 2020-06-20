document.addEventListener('DOMContentLoaded', ()=> {


    /* get csrf token */

    function getCsrf() {
        var inputElems = document.querySelectorAll('input');
        var csrfToken = '';
        for (i = 0; i < inputElems.length; ++i) {
            if (inputElems[i].name === 'csrfmiddlewaretoken') {
                csrfToken = inputElems[i].value;
                break;
            }
        }
        return csrfToken;
    };
    
    var tok = getCsrf('csrfmiddlewaretoken');
    input = document.querySelector('#token')
    input.setAttribute('value',tok)
    input.setAttribute('name','csrfmiddlewaretoken')
    console.log(tok)
        

    
    /* color of deleted items  */

    document.querySelectorAll('.borrado').forEach(td => {
        const borrar = td.parentElement;
        borrar.style.background = '#6b6a6a'
        borrar.children[0].style.textDecoration = 'line-through';
        borrar.children[1].style.textDecoration = 'line-through';
        borrar.children[2].style.textDecoration = 'line-through';
        borrar.children[3].style.textDecoration = 'line-through';
        borrar.children[4].style.textDecoration = 'line-through';
        borrar.children[5].style.textDecoration = 'line-through';
        borrar.children[6].style.textDecoration = 'line-through';
        borrar.children[7].style.textDecoration = 'line-through';
        borrar.children[8].style.textDecoration = 'line-through';
        borrar.children[9].style.textDecoration = 'line-through';
        borrar.children[10].style.textDecoration = 'line-through';
        
       
 
    });






    /* ajax request */

    document.querySelector('#formulario').onsubmit = () => {

        const request = new XMLHttpRequest();
        
    
        const fecha = document.querySelector('#fecha').value;
        const producto =document.querySelector('#producto').value;
        const lote = document.querySelector('#lote').value;
        const motivo = document.querySelector('#motivo').value;
        const tecnico = document.querySelector('#tecnico').value;
        const volumen = document.querySelector('#volumen').value;
        const guia = document.querySelector('#guia').value;
        const filtro = document.querySelector('#filtro').value;
        const linea = document.querySelector('#linea').value;
        const observaciones = document.querySelector('#observaciones').value;
        const token = document.querySelector('#token').value;

        

        

        request.open('POST' , "/formulario");


        request.onload = () => {
            const data = JSON.parse(request.responseText);
            const user = data.user
            const m = data.motivo
            const g = data.guia
            const f = data.filtro
            const t = data.tecnico
            const date = data.fecha
            const id = data.id
            
           
            if(data.success) {
                const tbody = document.querySelector('#tbody')
                const tr = document.createElement('tr')
                tr.setAttribute("id", "lista")
                const td1 = document.createElement('td')
                const td2 = document.createElement('td')
                const td3 = document.createElement('td')
                const td4 = document.createElement('td')
                const td5 = document.createElement('td')
                const td6 = document.createElement('td')
                const td7 = document.createElement('td')
                const td8 = document.createElement('td')
                const td9 = document.createElement('td')
                const td10 = document.createElement('td')
                const td11 = document.createElement('td')
                const td12 = document.createElement('td')
                const input = document.createElement('input')
                const input2 = document.createElement('input')
                const myForm = document.createElement('form')
                const button = document.createElement('button')
                myForm.setAttribute('action', "/remove");
                myForm.setAttribute('method', 'post');
                myForm.setAttribute('id', 'formulario3');
                input.setAttribute('type', 'hidden')
                input.setAttribute('value', id)
                input.setAttribute('name', 'remove')
                input2.setAttribute('type', 'hidden')
                input2.setAttribute('value', tok)
                input2.setAttribute('name', 'csrfmiddlewaretoken')
                button.setAttribute('class', "btn btn-danger")
                button.innerHTML = "Remove"
                myForm.append(input, input2, button)
                td12.append(myForm)

                





                
                td1.innerHTML = date 
                td2.innerHTML = producto 
                td3.innerHTML = lote 
                td4.innerHTML = m
                td5.innerHTML = t 
                td6.innerHTML = volumen 
                td7.innerHTML = g 
                td8.innerHTML = f 
                td9.innerHTML = linea 
                td10.innerHTML = observaciones
                td11.innerHTML = user
                tr.append(td1,td2,td3,td4,td5,td6,td7,td8,td9,td10,td11,td12,)
            
                tbody.insertBefore(tr, tbody.childNodes[0]);
               

                

                swal("Añadido", "El descarte fue añadido con exito", "success")
                document.querySelector('#lote').value = ""
                document.querySelector('#volumen').value = ""
                document.querySelector('#observaciones').value = ""
                document.querySelector('#lista').focus();



            }
            else{
                swal("there was an error")
            }

        }
        
        const data = new FormData();
        data.append('fecha', fecha);
        data.append('producto', producto);
        data.append('lote', lote);
        data.append('motivo', motivo);
        data.append('tecnico', tecnico);
        data.append('volumen', volumen);
        data.append('guia', guia);
        data.append('filtro', filtro);
        data.append('linea', linea);
        data.append('observaciones', observaciones);
        data.append('csrfmiddlewaretoken', token);
        

        request.send(data);
        return false;
    };


    


    
        









    
        
        
    








});