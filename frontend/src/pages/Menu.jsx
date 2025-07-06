import React, { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import { Badge } from '../components/ui/badge';
import { Button } from '../components/ui/button';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../components/ui/tabs';
import { menuItems } from '../data/mockData';

const Menu = () => {
  const [selectedCategory, setSelectedCategory] = useState('appetizers');

  const categories = [
    { id: 'appetizers', name: 'Appetizers', icon: '🥗' },
    { id: 'mains', name: 'Main Courses', icon: '🥩' },
    { id: 'desserts', name: 'Desserts', icon: '🍰' }
  ];

  return (
    <div className="min-h-screen bg-gray-50 pt-16">
      {/* Header */}
      <section className="bg-gradient-to-r from-amber-900 via-amber-800 to-amber-900 text-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">
            Our <span className="text-amber-300">Menu</span>
          </h1>
          <p className="text-xl md:text-2xl text-amber-100 max-w-3xl mx-auto leading-relaxed">
            Discover our carefully curated selection of gourmet dishes, crafted with the finest ingredients and culinary expertise
          </p>
        </div>
      </section>

      {/* Menu Section */}
      <section className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <Tabs value={selectedCategory} onValueChange={setSelectedCategory} className="w-full">
            <TabsList className="grid w-full grid-cols-3 mb-12 bg-white shadow-lg rounded-xl p-2">
              {categories.map((category) => (
                <TabsTrigger
                  key={category.id}
                  value={category.id}
                  className="flex items-center space-x-2 py-4 px-6 rounded-lg text-lg font-medium transition-all duration-300 data-[state=active]:bg-amber-600 data-[state=active]:text-white"
                >
                  <span className="text-2xl">{category.icon}</span>
                  <span>{category.name}</span>
                </TabsTrigger>
              ))}
            </TabsList>

            {categories.map((category) => (
              <TabsContent key={category.id} value={category.id} className="space-y-8">
                <div className="text-center mb-12">
                  <h2 className="text-4xl font-bold text-gray-900 mb-4 flex items-center justify-center">
                    <span className="text-5xl mr-4">{category.icon}</span>
                    {category.name}
                  </h2>
                  <div className="w-24 h-1 bg-amber-600 mx-auto rounded-full"></div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                  {menuItems[category.id]?.map((item) => (
                    <Card key={item.id} className="group hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 border-0 shadow-lg overflow-hidden">
                      <div className="relative overflow-hidden">
                        <img
                          src={item.image}
                          alt={item.name}
                          className="w-full h-48 object-cover group-hover:scale-110 transition-transform duration-300"
                        />
                        <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
                        <Badge className="absolute top-4 right-4 bg-amber-600 text-white text-lg px-3 py-1">
                          ${item.price}
                        </Badge>
                      </div>
                      <CardHeader>
                        <CardTitle className="text-xl font-bold text-gray-900 group-hover:text-amber-600 transition-colors duration-300">
                          {item.name}
                        </CardTitle>
                      </CardHeader>
                      <CardContent>
                        <p className="text-gray-600 leading-relaxed mb-4">
                          {item.description}
                        </p>
                        <div className="flex items-center justify-between">
                          <span className="text-2xl font-bold text-amber-600">
                            ${item.price}
                          </span>
                          <Button 
                            size="sm" 
                            className="bg-amber-600 hover:bg-amber-700 text-white transition-all duration-300 transform hover:scale-105"
                          >
                            Order Now
                          </Button>
                        </div>
                      </CardContent>
                    </Card>
                  ))}
                </div>
              </TabsContent>
            ))}
          </Tabs>
        </div>
      </section>

      {/* Menu Note */}
      <section className="py-16 bg-amber-50">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="bg-white rounded-2xl p-8 shadow-lg">
            <h3 className="text-2xl font-bold text-gray-900 mb-4">
              Chef's Special Note
            </h3>
            <p className="text-gray-600 leading-relaxed text-lg">
              All our dishes are prepared fresh daily using locally sourced ingredients. 
              We accommodate dietary restrictions and preferences - please inform your server 
              of any allergies or special requirements. Prices are subject to change based on 
              seasonal availability.
            </p>
            <div className="mt-6 pt-6 border-t border-gray-200">
              <p className="text-amber-600 font-semibold">
                For reservations and special requests, call us at (555) 123-4567
              </p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Menu;