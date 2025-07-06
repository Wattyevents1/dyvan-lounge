import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Button } from './ui/button';
import { Sheet, SheetContent, SheetDescription, SheetHeader, SheetTitle, SheetTrigger } from './ui/sheet';
import { Menu, X } from 'lucide-react';

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);
  const location = useLocation();

  const navigation = [
    { name: 'Home', href: '/' },
    { name: 'About', href: '/about' },
    { name: 'Menu', href: '/menu' },
    { name: 'Bar', href: '/bar' },
    { name: 'Gallery', href: '/gallery' },
    { name: 'Contact', href: '/contact' },
  ];

  const isActive = (path) => location.pathname === path;

  return (
    <nav className="bg-black/90 backdrop-blur-md fixed top-0 w-full z-50 transition-all duration-300">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link to="/" className="flex items-center">
            <span className="text-2xl font-bold text-amber-500 hover:text-amber-400 transition-colors duration-300">
              Serenity Lodge
            </span>
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden md:block">
            <div className="ml-10 flex items-baseline space-x-8">
              {navigation.map((item) => (
                <Link
                  key={item.name}
                  to={item.href}
                  className={`px-3 py-2 rounded-md text-sm font-medium transition-all duration-300 ${
                    isActive(item.href)
                      ? 'text-amber-500 bg-amber-500/10 shadow-lg shadow-amber-500/20'
                      : 'text-gray-300 hover:text-amber-400 hover:bg-white/10'
                  }`}
                >
                  {item.name}
                </Link>
              ))}
            </div>
          </div>

          {/* Reservation Button */}
          <div className="hidden md:block">
            <Link to="/reservations">
              <Button className="bg-amber-600 hover:bg-amber-700 text-white px-6 py-2 rounded-full transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-amber-500/25">
                Reserve Table
              </Button>
            </Link>
          </div>

          {/* Mobile menu button */}
          <div className="md:hidden">
            <Sheet open={isOpen} onOpenChange={setIsOpen}>
              <SheetTrigger asChild>
                <Button variant="ghost" size="icon" className="text-white">
                  <Menu className="h-6 w-6" />
                </Button>
              </SheetTrigger>
              <SheetContent side="right" className="w-[300px] bg-black/95 backdrop-blur-md border-amber-500/20">
                <SheetHeader>
                  <SheetTitle className="text-amber-500 text-xl">Serenity Lodge</SheetTitle>
                  <SheetDescription className="text-gray-400">
                    Luxury lounge & cottage experience
                  </SheetDescription>
                </SheetHeader>
                <div className="flex flex-col space-y-4 mt-8">
                  {navigation.map((item) => (
                    <Link
                      key={item.name}
                      to={item.href}
                      onClick={() => setIsOpen(false)}
                      className={`px-4 py-3 rounded-lg text-lg font-medium transition-all duration-300 ${
                        isActive(item.href)
                          ? 'text-amber-500 bg-amber-500/10 shadow-lg shadow-amber-500/20'
                          : 'text-gray-300 hover:text-amber-400 hover:bg-white/10'
                      }`}
                    >
                      {item.name}
                    </Link>
                  ))}
                  <Link to="/reservations" onClick={() => setIsOpen(false)}>
                    <Button className="w-full bg-amber-600 hover:bg-amber-700 text-white py-3 rounded-lg transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-amber-500/25 mt-6">
                      Reserve Table
                    </Button>
                  </Link>
                </div>
              </SheetContent>
            </Sheet>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;