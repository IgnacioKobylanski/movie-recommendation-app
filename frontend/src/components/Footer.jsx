import './Footer.css';

const Footer = () => {
  return (
    <footer className="footer">
      <div>
        <p>&copy; {new Date().getFullYear()} Mi Empresa. Todos los derechos reservados.</p>
        <nav>
          <ul className="footer-nav">
            <li>
              <a href="#">Términos y Condiciones</a>
            </li>
            <li>
              <a href="#">Política de Privacidad</a>
            </li>
            <li>
              <a href="#">Contacto</a>
            </li>
          </ul>
        </nav>
      </div>
    </footer>
  );
};

export default Footer;