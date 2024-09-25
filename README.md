# Django-Crud
.
# ClubTennis
REQUERIMIENTO:



DIAGRAMA ENTIDAD RELACIÓN:


HISTORIA DE USUARIO:


CASOS DE USO:


CASOS DE PRUEBA:


ATRIBUTOS DE CASOS DE PRUEBA:


DESARROLLO PROYECTO EN DJANGO:
*proyecto gral
setting.py
urls
*app asiganada
modelo.py
forms.py
urls.py
templates
Alta.html
baja.html
modificacionbes.html
listado.html


BASE DE DATOS:
phpMyAdmin


PRUEBAS FUNCIONALES BAJO SELENIUM:

PRUEBAS DE PERFOMANCE bajo BlazeMeter:


PROGRAMACIÓN CON PYTHON PARA EL ANALISIS DE DATOS: https://cursos.desafiolatam.com/courses/programacion-con-python-para-el-analisis-de-datos



Añadiendo seguridad al template base.html




{% load static %}
<!Doctype html>
<html lang="en">
  <head>
    <title>{% block titulo %}{% endblock titulo %}</title>
    
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS v5.0.2 -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"  integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

  </head>
  <body class="bg-success p-2 text-white">
    
    <!-- Modal para ingresar la clave -->
    <div class="modal fade" id="passwordModal" tabindex="-1" aria-labelledby="passwordModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="passwordModalLabel">Ingrese la clave</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="mb-3">
              <label for="passwordInput" class="form-label">Clave de acceso:</label>
              <input type="password" class="form-control" id="passwordInput" placeholder="Ingrese su clave">
              <div id="errorMsg" class="text-danger mt-2" style="display: none;">Clave incorrecta. Intente nuevamente.</div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
            <button type="button" class="btn btn-primary" id="passwordSubmit">Acceder</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Menu de Navegación -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">Navbar</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="{% url 'inicio' %}">Inicio</a>
              </li>
              <!-- Enlaces protegidos -->
              <li class="nav-item">
                <a class="nav-link protected-link" href="{% url 'listaCuota' %}" data-protected="true">Cuotas</a>
              </li>
              <li class="nav-item">
                <a class="nav-link protected-link" href="{% url 'lista' %}" data-protected="true">Jugadores</a>
              </li>
              <li class="nav-item">
                <a class="nav-link protected-link" href="{% url 'listaSocio' %}" data-protected="true">Socios</a>
              </li>
              <li class="nav-item">
                <a class="nav-link protected-link" href="{% url 'listaEvento' %}" data-protected="true">Eventos</a>
              </li>
              <li class="nav-item">
                <a class="nav-link " id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Nosotros
                </a>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
              </li>
            </ul>
            <form class="d-flex">
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
              <button class="btn btn-outline-success" type="submit">Search</button>
            </form>
          </div>
        </div>
      </nav>

      <div class="container">
        <div class="row">
            <div class="col-12">
              <br>
                {% block contenido %}{% endblock contenido %}
            </div>
        </div>
      </div>

    <!-- Bootstrap JavaScript Libraries -->
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>

    <!-- JavaScript para el manejo de clave -->
    <script>
      document.addEventListener('DOMContentLoaded', function () {
        const correctPassword = '12345';  // Cambia la clave aquí si es necesario
        const passwordInput = document.getElementById('passwordInput');
        const passwordSubmit = document.getElementById('passwordSubmit');
        const errorMsg = document.getElementById('errorMsg');
        
        // Al hacer clic en el botón de acceso
        passwordSubmit.addEventListener('click', function () {
          if (passwordInput.value === correctPassword) {
            // Si la clave es correcta, habilitar el acceso y cerrar el modal
            errorMsg.style.display = 'none';
            const protectedLinks = document.querySelectorAll('.protected-link');
            protectedLinks.forEach(link => link.removeAttribute('data-protected'));
            const modal = bootstrap.Modal.getInstance(document.getElementById('passwordModal'));
            modal.hide();
          } else {
            // Si la clave es incorrecta, mostrar mensaje de error
            errorMsg.style.display = 'block';
          }
        });

        // Mostrar el modal al intentar acceder a enlaces protegidos deshabilitados
        document.querySelectorAll('.protected-link').forEach(link => {
          link.addEventListener('click', function (event) {
            if (link.getAttribute('data-protected')) {
              event.preventDefault();  // Evita que el enlace se active
              const modal = new bootstrap.Modal(document.getElementById('passwordModal'));
              modal.show();  // Muestra el modal
            }
          });
        });
      });
    </script>
  </body>
</html>







