import React from "react";
import '../styles/Footer.css'
import { FaFacebookSquare} from "react-icons/fa";
import { FaSquareXTwitter } from "react-icons/fa6";
import { FaInstagram } from "react-icons/fa6";
import { IoLogoYoutube } from "react-icons/io5";

const Footer = () => {
  return (
      <footer>
          <p>&copy; {new Date().getFullYear()} MochiMovies. All rights reserved.</p>
          <div className="social-media">
          <FaFacebookSquare />
          <FaSquareXTwitter />
          <FaInstagram />
          <IoLogoYoutube />
          </div>
      </footer>
  );
};

export default Footer;