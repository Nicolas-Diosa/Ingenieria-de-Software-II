import unittest
from unittest.mock import patch, MagicMock
import requests

# Importamos las funciones directamente de tu archivo
from capa_seguridad_API import verificar_version, autenticar_y_sincronizar, obtener_localidades_api
import capa_seguridad_API

class TestCapaSeguridadAPI(unittest.TestCase):

    @patch('capa_seguridad_API.requests.get')
    def test_verificar_version_exitosa(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = "2" 
        mock_get.return_value = mock_response

        capa_seguridad_API.VERSION_LOCAL = 1
        resultado = verificar_version()
        
        self.assertEqual(resultado, 2)
        mock_get.assert_called_once_with(capa_seguridad_API.URL_VERSION)

    @patch('capa_seguridad_API.requests.get')
    def test_verificar_version_error(self, mock_get):
        mock_get.side_effect = requests.RequestException("Timeout de conexión")
        
        resultado = verificar_version()
        self.assertEqual(resultado, [])

    @patch('capa_seguridad_API.requests.post')      # Intercepta el POST de Login
    def test_login_exitoso(self, mock_post):
        
        mock_res_login = MagicMock()
        mock_res_login.status_code = 200
        mock_res_login.json.return_value = {
            "Usuario": "pam.meredy21",
            "Identificacion": "987204545",
            "Nombre": "Usuario Muestra"
        }
        mock_post.return_value = mock_res_login
        resultado = autenticar_y_sincronizar()

        self.assertTrue(resultado)

    @patch('capa_seguridad_API.requests.post')
    def test_login_fallido(self, mock_post):
        mock_res_login = MagicMock()
        mock_res_login.status_code = 400
        mock_post.return_value = mock_res_login
        resultado = autenticar_y_sincronizar()
        self.assertFalse(resultado)

    @patch('capa_seguridad_API.requests.get')
    def test_obtener_localidades_exitoso(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"AbreviacionCiudad": "BOG", "NombreCompleto": "Bogotá D.C."},
            {"AbreviacionCiudad": "CLO", "NombreCompleto": "Cali"}
        ]
        mock_get.return_value = mock_response

        resultado = obtener_localidades_api()

        self.assertEqual(len(resultado), 2)
        self.assertEqual(resultado[0]["AbreviacionCiudad"], "BOG")
        self.assertEqual(resultado[0]["NombreCompleto"], "Bogotá D.C.")
        self.assertEqual(resultado[1]["AbreviacionCiudad"], "CLO")
        self.assertEqual(resultado[1]["NombreCompleto"], "Cali")

    @patch('capa_seguridad_API.requests.get')
    def test_obtener_localidades_error_500(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        resultado = obtener_localidades_api()

        self.assertEqual(resultado, [])

if __name__ == '__main__':
    unittest.main()