#para ejecutar los tests escribe en terminal: python -m unittest discover -s tests -v

import os
import sys
import unittest
from unittest.mock import patch


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_DIR = os.path.join(ROOT_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from order_system import OrderSystem


class TestOrderSystem(unittest.TestCase):

    def setUp(self):
        self.system = OrderSystem()
        self.regular_user_co = {"type": "regular", "country": "CO"}
        self.premium_user_us = {"type": "premium", "country": "US"}
        self.vip_user_co = {"type": "vip", "country": "CO", "email": "vip@example.com"}
        self.small_items = [{"price": 100, "quantity": 2}]
        self.large_items = [{"price": 400, "quantity": 2}]

    def test_create_order_basic(self):
        """Debe crear una orden correctamente."""
        order = self.system.create_order(self.regular_user_co, self.small_items, "cash")

        # ✅ Este test debería PASAR incluso con el código original
        # porque la creación básica sí funciona.
        self.assertIsNotNone(order)
        self.assertEqual(order["status"], "created")
        self.assertEqual(len(self.system.orders), 1)

    def test_total_regular_user_with_co_shipping(self):
        order = self.system.create_order(self.regular_user_co, self.small_items, "card")

        expected_total = 100 * 2 * 0.95 * 1.19 + 20000
        # Este test puede FALLAR si hay errores en descuentos o impuestos
        self.assertAlmostEqual(order["total"], expected_total)

    def test_total_premium_user_international(self):
        """Valida descuento premium + envío internacional."""
        order = self.system.create_order(self.premium_user_us, self.small_items, "paypal")
        expected_total = 100 * 2 * 0.90 * 1.19 + 50000

        # ⚠️ Puede FALLAR si el orden de operaciones es incorrecto
        self.assertAlmostEqual(order["total"], expected_total)

    def test_total_vip_user_discount_extra(self):
        """Valida descuento VIP + descuento extra por >500."""
        order = self.system.create_order(self.vip_user_co, self.large_items, "cash")

        expected_total = 400 * 2 * 0.80 * 0.95 * 1.19 + 20000

        # Aquí se detecta si el descuento adicional está mal aplicado
        self.assertAlmostEqual(order["total"], expected_total)

    def test_invalid_payment_raises_exception(self):
        """Debe lanzar excepción si el método de pago es inválido."""

        # Este test debería PASAR con el código original
        with self.assertRaises(Exception) as context:
            self.system.create_order(self.regular_user_co, self.small_items, "bitcoin")

        self.assertIn("Método de pago inválido", str(context.exception))

    def test_order_id_is_valid(self):
        """El ID debe ser un float entre 0 y 1."""
        order = self.system.create_order(self.regular_user_co, self.small_items, "cash")

        # Debe PASAR: random.random() cumple esto
        self.assertIsInstance(order["id"], float)
        self.assertGreaterEqual(order["id"], 0)
        self.assertLess(order["id"], 1)

    @patch("builtins.print")
    def test_payment_card_print(self, mock_print):
        """Verifica que se imprime el mensaje correcto para tarjeta."""
        self.system.create_order(self.regular_user_co, self.small_items, "card")

        # Debe PASAR si el print está bien implementado
        mock_print.assert_any_call("Procesando tarjeta...")

    def test_unknown_user_type_no_discount(self):
        """Usuario con tipo desconocido NO debería recibir descuento."""
        user = {"type": "unknown", "country": "CO"}
        order = self.system.create_order(user, self.small_items, "cash")
        expected_total = 100 * 2 * 1.19 + 20000

        # Este test puede FALLAR dependiendo del diseño esperado
        self.assertAlmostEqual(order["total"], expected_total)


if __name__ == "__main__":
    unittest.main()