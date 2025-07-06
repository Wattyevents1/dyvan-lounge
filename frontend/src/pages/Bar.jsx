import React, { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import { Badge } from '../components/ui/badge';
import { Button } from '../components/ui/button';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../components/ui/tabs';
import { Clock, Star, Wine, Sparkles } from 'lucide-react';
import { cocktails, wines, specialOffers } from '../data/mockData';

const Bar = () => {
  const [selectedCategory, setSelectedCategory] = useState('signature');

  const drinkCategories = [
    { id: 'signature', name: 'Signature Cocktails', icon: '🍸' },
    { id: 'classic', name: 'Classic Cocktails', icon: '🥃' },
    { id: 'wines', name: 'Wine Selection', icon: '🍷' }
  ];

  const filteredCocktails = cocktails.filter(cocktail => cocktail.category === selectedCategory);

  return (
    <div className="min-h-screen bg-gray-50 pt-16">
      {/* Header */}
      <section className="bg-gradient-to-r from-gray-900 via-black to-gray-900 text-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h1 className="text-5xl md:text-6xl font-bold mb-6">
            The <span className="text-amber-500">Bar</span>
          </h1>
          <p className="text-xl md:text-2xl text-gray-300 max-w-3xl mx-auto leading-relaxed">
            Discover our carefully crafted cocktails and premium wine collection, curated by master mixologists
          </p>
        </div>
      </section>

      {/* Happy Hour Banner */}
      <section className="bg-amber-600 text-white py-6">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-center space-x-4">
            <Sparkles className="h-6 w-6 text-amber-200" />
            <div className="text-center">
              <h3 className="text-lg font-bold">Happy Hour Special</h3>
              <p className="text-amber-100">50% off all cocktails | Monday - Friday, 5:00 PM - 7:00 PM</p>
            </div>
            <Sparkles className="h-6 w-6 text-amber-200" />
          </div>
        </div>
      </section>

      {/* Drinks Menu */}
      <section className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <Tabs value={selectedCategory} onValueChange={setSelectedCategory} className="w-full">
            <TabsList className="grid w-full grid-cols-3 mb-12 bg-white shadow-lg rounded-xl p-2">
              {drinkCategories.map((category) => (
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

            {/* Cocktails */}
            <TabsContent value="signature" className="space-y-8">
              <div className="text-center mb-12">
                <h2 className="text-4xl font-bold text-gray-900 mb-4 flex items-center justify-center">
                  <span className="text-5xl mr-4">🍸</span>
                  Signature Cocktails
                </h2>
                <div className="w-24 h-1 bg-amber-600 mx-auto rounded-full"></div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                {filteredCocktails.map((cocktail) => (
                  <Card key={cocktail.id} className="group hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 border-0 shadow-lg overflow-hidden">
                    <div className="relative overflow-hidden">
                      <img
                        src={cocktail.image}
                        alt={cocktail.name}
                        className="w-full h-48 object-cover group-hover:scale-110 transition-transform duration-300"
                      />
                      <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
                      <Badge className="absolute top-4 right-4 bg-amber-600 text-white text-lg px-3 py-1">
                        ${cocktail.price}
                      </Badge>
                      <Badge className="absolute top-4 left-4 bg-black/70 text-white">
                        <Star className="h-4 w-4 mr-1" />
                        Signature
                      </Badge>
                    </div>
                    <CardHeader>
                      <CardTitle className="text-xl font-bold text-gray-900 group-hover:text-amber-600 transition-colors duration-300">
                        {cocktail.name}
                      </CardTitle>
                    </CardHeader>
                    <CardContent>
                      <p className="text-gray-600 leading-relaxed mb-4">
                        {cocktail.description}
                      </p>
                      <div className="flex items-center justify-between">
                        <span className="text-2xl font-bold text-amber-600">
                          ${cocktail.price}
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

            <TabsContent value="classic" className="space-y-8">
              <div className="text-center mb-12">
                <h2 className="text-4xl font-bold text-gray-900 mb-4 flex items-center justify-center">
                  <span className="text-5xl mr-4">🥃</span>
                  Classic Cocktails
                </h2>
                <div className="w-24 h-1 bg-amber-600 mx-auto rounded-full"></div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                {filteredCocktails.map((cocktail) => (
                  <Card key={cocktail.id} className="group hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 border-0 shadow-lg overflow-hidden">
                    <div className="relative overflow-hidden">
                      <img
                        src={cocktail.image}
                        alt={cocktail.name}
                        className="w-full h-48 object-cover group-hover:scale-110 transition-transform duration-300"
                      />
                      <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
                      <Badge className="absolute top-4 right-4 bg-amber-600 text-white text-lg px-3 py-1">
                        ${cocktail.price}
                      </Badge>
                    </div>
                    <CardHeader>
                      <CardTitle className="text-xl font-bold text-gray-900 group-hover:text-amber-600 transition-colors duration-300">
                        {cocktail.name}
                      </CardTitle>
                    </CardHeader>
                    <CardContent>
                      <p className="text-gray-600 leading-relaxed mb-4">
                        {cocktail.description}
                      </p>
                      <div className="flex items-center justify-between">
                        <span className="text-2xl font-bold text-amber-600">
                          ${cocktail.price}
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

            <TabsContent value="wines" className="space-y-8">
              <div className="text-center mb-12">
                <h2 className="text-4xl font-bold text-gray-900 mb-4 flex items-center justify-center">
                  <span className="text-5xl mr-4">🍷</span>
                  Wine Selection
                </h2>
                <div className="w-24 h-1 bg-amber-600 mx-auto rounded-full"></div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                {wines.map((wine) => (
                  <Card key={wine.id} className="group hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 border-0 shadow-lg">
                    <CardHeader>
                      <div className="flex items-center justify-between">
                        <CardTitle className="text-xl font-bold text-gray-900 group-hover:text-amber-600 transition-colors duration-300">
                          {wine.name}
                        </CardTitle>
                        <Badge className={`${
                          wine.type === 'red' ? 'bg-red-600' : 
                          wine.type === 'white' ? 'bg-green-600' : 
                          'bg-amber-600'
                        } text-white`}>
                          {wine.type}
                        </Badge>
                      </div>
                      <p className="text-amber-600 font-semibold flex items-center">
                        <Wine className="h-4 w-4 mr-2" />
                        {wine.region}
                      </p>
                    </CardHeader>
                    <CardContent>
                      <p className="text-gray-600 leading-relaxed mb-4">
                        {wine.description}
                      </p>
                      <div className="flex items-center justify-between">
                        <span className="text-2xl font-bold text-amber-600">
                          ${wine.price}
                        </span>
                        <Button 
                          size="sm" 
                          className="bg-amber-600 hover:bg-amber-700 text-white transition-all duration-300 transform hover:scale-105"
                        >
                          Order Bottle
                        </Button>
                      </div>
                    </CardContent>
                  </Card>
                ))}
              </div>
            </TabsContent>
          </Tabs>
        </div>
      </section>

      {/* Special Offers */}
      <section className="py-20 bg-gray-900 text-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-bold mb-4">
              Bar <span className="text-amber-500">Specials</span>
            </h2>
            <p className="text-xl text-gray-300 max-w-3xl mx-auto">
              Don't miss our exclusive drink specials and seasonal promotions
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {specialOffers.map((offer) => (
              <Card key={offer.id} className="bg-gray-800 border-gray-700 group hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 overflow-hidden">
                <div className="relative overflow-hidden">
                  <img
                    src={offer.image}
                    alt={offer.title}
                    className="w-full h-48 object-cover group-hover:scale-110 transition-transform duration-300"
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent" />
                  <div className="absolute bottom-4 left-4 text-white">
                    <h3 className="text-2xl font-bold mb-2">{offer.title}</h3>
                    <p className="text-amber-200 flex items-center">
                      <Clock className="mr-2 h-4 w-4" />
                      {offer.time}
                    </p>
                  </div>
                </div>
                <CardContent className="p-6">
                  <p className="text-gray-300 leading-relaxed">{offer.description}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Bar Information */}
      <section className="py-16 bg-amber-50">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="bg-white rounded-2xl p-8 shadow-lg">
            <h3 className="text-2xl font-bold text-gray-900 mb-4">
              Bar Information
            </h3>
            <p className="text-gray-600 leading-relaxed text-lg mb-6">
              Our bar features an extensive selection of premium spirits, craft cocktails, and fine wines. 
              All cocktails are made with fresh ingredients and premium liquors. We're happy to accommodate 
              special requests and dietary restrictions.
            </p>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 text-left">
              <div>
                <h4 className="font-semibold text-gray-900 mb-2">Bar Hours</h4>
                <p className="text-gray-600">
                  Monday - Thursday: 5:00 PM - 12:00 AM<br />
                  Friday - Saturday: 5:00 PM - 2:00 AM<br />
                  Sunday: 4:00 PM - 11:00 PM
                </p>
              </div>
              <div>
                <h4 className="font-semibold text-gray-900 mb-2">Reservations</h4>
                <p className="text-gray-600">
                  Bar seating is first-come, first-served<br />
                  For table reservations: (555) 123-4567<br />
                  Private events welcomed
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Bar;