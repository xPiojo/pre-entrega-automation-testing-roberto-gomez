import requests
from utils.logger import logger

def test_api_get_posts(api_url):
    """
    1. GET: Verificar la obtención de la lista de posts.
    """

    logger.info("\n" + "="*50)
    logger.info("🚀 INICIO TEST API: GET /posts")
    logger.info("="*50)
    
    endpoint = f"{api_url}/posts"
    logger.info(f"STEP 1: Consultando endpoint GET {endpoint}...")
    
    response = requests.get(endpoint)
    
    logger.info("STEP 2: Verificando código de estado...")
    assert response.status_code == 200, f"Error: Esperado 200, recibido {response.status_code}."
    logger.info("✅ Código de estado 200 verificado.")
    
    logger.info("STEP 3: Verificando contenido...")
    posts = response.json()
    assert isinstance(posts, list), "Error: La respuesta no es una lista."
    assert len(posts) > 0, "Error: La lista está vacía."
    logger.info(f"✅ Respuesta válida: Se encontraron {len(posts)} posts.")
    
    logger.info("--- FIN DEL TEST ---\n") 


def test_api_create_post(api_url):
    """
    2. POST: Verificar la creación de un nuevo post.
    """
    # ENCABEZADO MEJORADO
    logger.info("\n" + "="*50)
    logger.info("🚀 INICIO TEST API: POST /posts")
    logger.info("="*50)
    
    endpoint = f"{api_url}/posts"
    logger.info(f"STEP 1: Enviando solicitud POST a {endpoint}...")
    
    new_post = {
        "title": "Nuevo Post QA",
        "body": "Contenido del post de prueba",
        "userId": 1
    }

    response = requests.post(endpoint, json=new_post)
    
    logger.info("STEP 2: Verificando código de estado...")
    assert response.status_code == 201, f"Error: Esperado 201, recibido {response.status_code}."
    logger.info("✅ Código de estado 201 (Created) verificado.")
    
    logger.info("STEP 3: Verificando respuesta...")
    created_post = response.json()
    assert "id" in created_post, "Error: No se recibió ID del nuevo post."
    logger.info(f"✅ Post creado correctamente con ID: {created_post['id']}.")
    
    logger.info("--- FIN DEL TEST ---\n")


def test_api_update_post(api_url):
    """
    3. PUT: Verificar la actualización completa de un post.
    """
    
    logger.info("\n" + "="*50)
    logger.info("🚀 INICIO TEST API: PUT /posts/1")
    logger.info("="*50)

    endpoint = f"{api_url}/posts/1"
    logger.info(f"STEP 1: Enviando solicitud PUT a {endpoint}...")

    post_update = {
        "title": "Post Actualizado",
        "body": "Contenido actualizado del post",
        "userId": 1
    }

    response = requests.put(endpoint, json=post_update)

    logger.info("STEP 2: Verificando código de estado...")
    assert response.status_code == 200, f"Error: Esperado 200, recibido {response.status_code}."
    logger.info("✅ Código de estado 200 verificado.")

    data = response.json()
    assert data['title'] == "Post Actualizado", "Error: El título no se actualizó."
    logger.info("✅ Datos validados: El título coincide con el enviado.")

    logger.info("--- FIN DEL TEST ---\n")


def test_api_delete_post(api_url):
    """
    4. DELETE: Verificar el borrado de un post.
    """
    
    logger.info("\n" + "="*50)
    logger.info("🚀 INICIO TEST API: DELETE /posts/1")
    logger.info("="*50)
    
    endpoint = f"{api_url}/posts/1"
    logger.info(f"STEP 1: Enviando solicitud DELETE a {endpoint}...")
    
    response = requests.delete(endpoint)
    
    logger.info("STEP 2: Verificando código de estado...")
    assert response.status_code == 200, f"Error: Esperado 200, recibido {response.status_code}."
    logger.info("✅ Código de estado 200 verificado (Recurso eliminado).")
    
    logger.info("--- FIN DEL TEST ---\n")