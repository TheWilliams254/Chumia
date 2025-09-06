// components/Navbar.jsx
import { useState } from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  return (
    <nav className="bg-gray-900 text-white shadow-md fixed w-full z-50">
      <div className="container mx-auto px-4 flex justify-between items-center py-4">
        {/* Logo */}
        <div className="flex items-center space-x-2">
          <i className="fas fa-tools text-yellow-400 text-2xl"></i>
          <span className="font-bold text-xl">CHUMIA</span>
        </div>

        {/* Desktop Menu */}
        <ul className="hidden md:flex space-x-6">
          <li><a href="#hero" className="hover:text-yellow-400 transition-colors">Home</a></li>
          <li><a href="#products" className="hover:text-yellow-400 transition-colors">Products</a></li>
          <li><a href="#workshops" className="hover:text-yellow-400 transition-colors">Workshops</a></li>
          <li><a href="#about" className="hover:text-yellow-400 transition-colors">About</a></li>
          <li><a href="#contact" className="hover:text-yellow-400 transition-colors">Contact</a></li>
        </ul>

        {/* Desktop Buttons */}
        <div className="hidden md:flex space-x-4">
        <Link
            to="/login"
            className="bg-yellow-400 text-gray-900 px-4 py-2 rounded-md hover:bg-yellow-300 transition-colors"
        >
        Login
  </Link>
  <Link
    to="/register"
    className="border border-yellow-400 px-4 py-2 rounded-md hover:bg-yellow-400 hover:text-gray-900 transition-colors"
  >
    Sign Up
  </Link>
</div>

        {/* Mobile Menu Button */}
        <button
          className="md:hidden focus:outline-none"
          onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
        >
          <i className="fas fa-bars text-xl"></i>
        </button>
      </div>

      {/* Mobile menu */}
{mobileMenuOpen && (
  <div className="md:hidden bg-gray-800">
    <ul className="flex flex-col px-4 py-2 space-y-2">
      <li><Link to="/" className="block py-2 hover:text-yellow-400 transition-colors">Home</Link></li>
      <li><Link to="/products" className="block py-2 hover:text-yellow-400 transition-colors">Products</Link></li>
      <li><Link to="/workshops" className="block py-2 hover:text-yellow-400 transition-colors">Workshops</Link></li>
      <li><Link to="/about" className="block py-2 hover:text-yellow-400 transition-colors">About</Link></li>
      <li><Link to="/contact" className="block py-2 hover:text-yellow-400 transition-colors">Contact</Link></li>
      <li>
        <Link
          to="/login"
          className="w-full bg-yellow-400 text-gray-900 py-2 rounded-md mt-2 hover:bg-yellow-300 transition-colors block text-center"
        >
          Login
        </Link>
      </li>
      <li>
        <Link
          to="/register"
          className="w-full border border-yellow-400 text-white py-2 rounded-md mt-1 hover:bg-yellow-400 hover:text-gray-900 transition-colors block text-center"
        >
          Sign Up
        </Link>
      </li>
    </ul>
  </div>
)}

  </nav>
  );
};

export default Navbar;
