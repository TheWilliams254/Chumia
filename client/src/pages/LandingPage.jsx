// pages/LandingPage.jsx
import Navbar from "../components/Navbar";
import { useState } from "react";


const testimonials = [
  {
    name: "Robert Johnson",
    role: "Contractor",
    image: "https://cdn.pixabay.com/photo/2017/08/12/18/31/male-2634974_1280.jpg",
    text: "Chumia has completely transformed how I source materials for my construction projects. The quality of products and ease of ordering is unmatched!"
  },
  {
    name: "Michael Smith",
    role: "Foreman",
    image: "https://cdn.pixabay.com/photo/2016/11/21/12/42/beard-1845166_1280.jpg",
    text: "As a foreman, I need reliable suppliers. The workshop owners on Chumia deliver quality materials on time, every time. Highly recommended!"
  },
  {
    name: "Sarah Williams",
    role: "Workshop Owner",
    image: "https://cdn.pixabay.com/photo/2016/11/29/09/38/adult-1868750_1280.jpg",
    text: "I registered my metal workshop on Chumia and saw a 40% increase in orders within the first month. The platform connects us directly with customers!"
  }
];

const LandingPage = () => {
  return (
    <div className="bg-gray-50 text-gray-800">
      {/* Navbar */}
      <Navbar />

      {/* Hero Section */}
      <header id="hero" className="bg-yellow-400 pt-24">
        <div className="container mx-auto px-4 py-20 text-center">
          <h1 className="text-4xl md:text-5xl font-bold mb-4 text-gray-900">
            Discover a Better Way to Source Building Materials
          </h1>
          <p className="text-lg md:text-xl mb-6 text-gray-800 max-w-2xl mx-auto">
            Chumia connects contractors, foremen, and workshop owners directly
            for seamless material sourcing and sales.
          </p>
          <div className="flex justify-center gap-4">
            <button className="bg-gray-900 text-yellow-400 px-6 py-3 rounded-md hover:bg-gray-800 transition-colors">
              Get Started
            </button>
            <button className="border border-gray-900 text-gray-900 px-6 py-3 rounded-md hover:bg-gray-900 hover:text-yellow-400 transition-colors">
              Learn More
            </button>
          </div>
        </div>
      </header>

      {/* Features Section */}
      <section id="features" className="py-20 bg-gray-50">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-3xl font-bold mb-12">Why Choose Chumia?</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="bg-white shadow-md p-6 rounded-lg">
              <i className="fas fa-truck text-yellow-400 text-4xl mb-4"></i>
              <h3 className="font-bold text-xl mb-2">Fast Delivery</h3>
              <p className="text-gray-600">
                Get building materials delivered to your site quickly and reliably.
              </p>
            </div>
            <div className="bg-white shadow-md p-6 rounded-lg">
              <i className="fas fa-cubes text-yellow-400 text-4xl mb-4"></i>
              <h3 className="font-bold text-xl mb-2">Wide Selection</h3>
              <p className="text-gray-600">
                Browse a variety of windows, doors, metals, and other construction items.
              </p>
            </div>
            <div className="bg-white shadow-md p-6 rounded-lg">
              <i className="fas fa-handshake text-yellow-400 text-4xl mb-4"></i>
              <h3 className="font-bold text-xl mb-2">Trusted Workshops</h3>
              <p className="text-gray-600">
                Connect directly with verified workshop owners for quality assurance.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Call to Action */}
      <section id="cta" className="py-20 bg-yellow-400">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-3xl md:text-4xl font-bold mb-6 text-gray-800">
            Ready to Get Started?
          </h2>
          <p className="text-lg mb-8 text-gray-700 max-w-2xl mx-auto">
            Join Chumia today and discover a better way to source building materials or showcase your workshop products.
          </p>
          <div className="flex flex-col sm:flex-row justify-center gap-4">
            <button className="bg-gray-900 text-yellow-400 px-8 py-3 rounded-md text-lg font-semibold">
              Sign Up Now
            </button>
            <button className="bg-gray-100 text-gray-900 px-8 py-3 rounded-md text-lg font-semibold">
              Learn More
            </button>
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section id="testimonials" className="py-16 bg-gray-800 text-white">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl font-bold mb-10 text-center">What Our Customers Say</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {testimonials.map((t, idx) => (
              <div key={idx} className="bg-gray-700 p-6 rounded-lg relative">
                <div className="text-yellow-400 text-4xl absolute -top-4 left-4 opacity-50">
                  <i className="fas fa-quote-left"></i>
                </div>
                <div className="pt-6">
                  <p className="mb-4">{t.text}</p>
                  <div className="flex items-center">
                    <div className="w-12 h-12 rounded-full overflow-hidden mr-4">
                      <img src={t.image} alt={t.name} className="w-full h-full object-cover"/>
                    </div>
                    <div>
                      <h4 className="font-bold">{t.name}</h4>
                      <p className="text-sm text-gray-300">{t.role}</p>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer id="footer" className="bg-gray-900 text-white py-12">
        <div className="container mx-auto px-4">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <div>
              <div className="flex items-center mb-4">
                <i className="fas fa-tools text-yellow-400 mr-2 text-2xl"></i>
                <span className="text-xl font-bold">CHUMIA</span>
              </div>
              <p className="text-gray-400 mb-4">
                The premier marketplace for building materials and workshop items.
              </p>
              <div className="flex space-x-4">
                <i className="fab fa-facebook-f text-gray-400 hover:text-yellow-400 cursor-pointer"></i>
                <i className="fab fa-twitter text-gray-400 hover:text-yellow-400 cursor-pointer"></i>
                <i className="fab fa-instagram text-gray-400 hover:text-yellow-400 cursor-pointer"></i>
                <i className="fab fa-linkedin-in text-gray-400 hover:text-yellow-400 cursor-pointer"></i>
              </div>
            </div>
            <div>
              <h3 className="text-lg font-bold mb-4">Quick Links</h3>
              <ul className="space-y-2 text-gray-400">
                <li className="hover:text-yellow-400 cursor-pointer">Home</li>
                <li className="hover:text-yellow-400 cursor-pointer">Browse Products</li>
                <li className="hover:text-yellow-400 cursor-pointer">Workshop Owners</li>
                <li className="hover:text-yellow-400 cursor-pointer">About Us</li>
                <li className="hover:text-yellow-400 cursor-pointer">Contact</li>
              </ul>
            </div>
            <div>
              <h3 className="text-lg font-bold mb-4">Categories</h3>
              <ul className="space-y-2 text-gray-400">
                <li className="hover:text-yellow-400 cursor-pointer">Windows</li>
                <li className="hover:text-yellow-400 cursor-pointer">Doors</li>
                <li className="hover:text-yellow-400 cursor-pointer">Metal Furniture</li>
                <li className="hover:text-yellow-400 cursor-pointer">Cookers</li>
                <li className="hover:text-yellow-400 cursor-pointer">Curtain Materials</li>
              </ul>
            </div>
            <div>
              <h3 className="text-lg font-bold mb-4">Contact Us</h3>
              <p className="text-gray-400">123 Workshop Avenue, Industrial District</p>
              <p className="text-gray-400">+254 123 456 789</p>
              <p className="text-gray-400">info@chumia.com</p>
            </div>
          </div>
          <div className="border-t border-gray-800 mt-10 pt-6 flex flex-col md:flex-row justify-between items-center text-gray-400 text-sm">
            <p>&copy; 2025 Chumia. All rights reserved.</p>
            <div className="mt-4 md:mt-0 flex space-x-4">
              <span className="hover:text-yellow-400 cursor-pointer">Privacy Policy</span>
              <span className="hover:text-yellow-400 cursor-pointer">Terms of Service</span>
              <span className="hover:text-yellow-400 cursor-pointer">Shipping Information</span>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default LandingPage;
