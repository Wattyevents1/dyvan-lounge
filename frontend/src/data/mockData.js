// Mock data for the lounge and cottage website

export const heroImages = [
  "https://images.unsplash.com/photo-1580719996124-1b5c300d251a",
  "https://images.unsplash.com/photo-1700874897288-27ae7ab28ee7", 
  "https://images.pexels.com/photos/29046927/pexels-photo-29046927.jpeg",
  "https://images.pexels.com/photos/18866153/pexels-photo-18866153.jpeg",
  "https://images.pexels.com/photos/7476832/pexels-photo-7476832.jpeg"
];

export const menuItems = {
  appetizers: [
    {
      id: 1,
      name: "Truffle Arancini",
      description: "Crispy risotto balls with truffle oil, parmesan, and herb aioli",
      price: 16,
      image: "https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b"
    },
    {
      id: 2,
      name: "Burrata & Prosciutto",
      description: "Creamy burrata, aged prosciutto, grilled peach, and balsamic reduction",
      price: 18,
      image: "https://images.unsplash.com/photo-1571091655789-405eb7a3a3a8"
    },
    {
      id: 3,
      name: "Oysters Rockefeller",
      description: "Fresh oysters with creamed spinach, herbs, and breadcrumb crust",
      price: 22,
      image: "https://images.unsplash.com/photo-1606731426118-a733c2499b13"
    },
    {
      id: 4,
      name: "Charcuterie Board",
      description: "Selection of artisanal meats, cheeses, nuts, and preserves",
      price: 24,
      image: "https://images.unsplash.com/photo-1504674900247-0877df9cc836"
    }
  ],
  mains: [
    {
      id: 5,
      name: "Wagyu Beef Tenderloin",
      description: "8oz prime cut with roasted vegetables and red wine reduction",
      price: 48,
      image: "https://images.unsplash.com/photo-1546833999-b9f581a1996d"
    },
    {
      id: 6,
      name: "Pan-Seared Salmon",
      description: "Atlantic salmon with quinoa pilaf and lemon butter sauce",
      price: 32,
      image: "https://images.unsplash.com/photo-1467003909585-2f8a72700288"
    },
    {
      id: 7,
      name: "Duck Confit",
      description: "Slow-cooked duck leg with cherry gastrique and wild rice",
      price: 36,
      image: "https://images.unsplash.com/photo-1544025162-d76694265947"
    },
    {
      id: 8,
      name: "Lobster Risotto",
      description: "Creamy arborio rice with fresh lobster and microgreens",
      price: 42,
      image: "https://images.unsplash.com/photo-1611599548918-d1085825c2e8"
    }
  ],
  desserts: [
    {
      id: 9,
      name: "Chocolate Lava Cake",
      description: "Warm chocolate cake with molten center and vanilla ice cream",
      price: 12,
      image: "https://images.unsplash.com/photo-1606313564200-e75d5e30476c"
    },
    {
      id: 10,
      name: "Crème Brûlée",
      description: "Classic vanilla custard with caramelized sugar crust",
      price: 10,
      image: "https://images.unsplash.com/photo-1470124182917-cc6e71b22ecc"
    },
    {
      id: 11,
      name: "Tiramisu",
      description: "Traditional Italian dessert with espresso and mascarpone",
      price: 11,
      image: "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9"
    }
  ]
};

export const cocktails = [
  {
    id: 1,
    name: "Serenity Sunset",
    description: "Bourbon, peach liqueur, honey, lemon, and fresh thyme",
    price: 16,
    image: "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b",
    category: "signature"
  },
  {
    id: 2,
    name: "Mountain Mist",
    description: "Gin, elderflower, cucumber, lime, and rosemary smoke",
    price: 15,
    image: "https://images.unsplash.com/photo-1551538827-9c037cb4f32a",
    category: "signature"
  },
  {
    id: 3,
    name: "Lodge Old Fashioned",
    description: "Rye whiskey, maple syrup, orange bitters, and smoked cherry",
    price: 18,
    image: "https://images.unsplash.com/photo-1470337458703-46ad1756a187",
    category: "signature"
  },
  {
    id: 4,
    name: "Classic Martini",
    description: "Premium vodka or gin, dry vermouth, olive or lemon twist",
    price: 14,
    image: "https://images.unsplash.com/photo-1541746972996-4e0b0f93e586",
    category: "classic"
  },
  {
    id: 5,
    name: "Negroni",
    description: "Gin, Campari, sweet vermouth, orange peel",
    price: 13,
    image: "https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd",
    category: "classic"
  },
  {
    id: 6,
    name: "Whiskey Sour",
    description: "Bourbon, lemon juice, simple syrup, egg white",
    price: 12,
    image: "https://images.unsplash.com/photo-1560512823-829485b8bf24",
    category: "classic"
  }
];

export const wines = [
  {
    id: 1,
    name: "Château Margaux 2015",
    description: "Bordeaux red wine with notes of blackberry and cedar",
    price: 85,
    type: "red",
    region: "Bordeaux, France"
  },
  {
    id: 2,
    name: "Chablis Premier Cru",
    description: "Crisp white wine with mineral notes and citrus finish",
    price: 45,
    type: "white",
    region: "Burgundy, France"
  },
  {
    id: 3,
    name: "Caymus Napa Valley Cabernet",
    description: "Full-bodied red with dark fruit flavors and smooth tannins",
    price: 68,
    type: "red",
    region: "Napa Valley, CA"
  },
  {
    id: 4,
    name: "Dom Pérignon 2012",
    description: "Prestigious champagne with fine bubbles and complex flavors",
    price: 280,
    type: "sparkling",
    region: "Champagne, France"
  }
];

export const galleryImages = [
  {
    id: 1,
    url: "https://images.unsplash.com/photo-1580719996124-1b5c300d251a",
    category: "interior",
    title: "Lounge Interior"
  },
  {
    id: 2,
    url: "https://images.unsplash.com/photo-1700874897288-27ae7ab28ee7",
    category: "dining",
    title: "Dining Experience"
  },
  {
    id: 3,
    url: "https://images.pexels.com/photos/29046927/pexels-photo-29046927.jpeg",
    category: "interior",
    title: "Elegant Seating"
  },
  {
    id: 4,
    url: "https://images.pexels.com/photos/18866153/pexels-photo-18866153.jpeg",
    category: "dining",
    title: "Fine Dining"
  },
  {
    id: 5,
    url: "https://images.pexels.com/photos/7476832/pexels-photo-7476832.jpeg",
    category: "bar",
    title: "Bar Area"
  },
  {
    id: 6,
    url: "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b",
    category: "bar",
    title: "Craft Cocktails"
  },
  {
    id: 7,
    url: "https://images.unsplash.com/photo-1551538827-9c037cb4f32a",
    category: "bar",
    title: "Signature Drinks"
  },
  {
    id: 8,
    url: "https://images.unsplash.com/photo-1544025162-d76694265947",
    category: "food",
    title: "Gourmet Cuisine"
  }
];

export const specialOffers = [
  {
    id: 1,
    title: "Happy Hour Special",
    description: "50% off all cocktails and appetizers",
    time: "Monday - Friday, 5:00 PM - 7:00 PM",
    image: "https://images.unsplash.com/photo-1551538827-9c037cb4f32a"
  },
  {
    id: 2,
    title: "Wine Wednesday",
    description: "30% off all wines by the bottle",
    time: "Every Wednesday, All Day",
    image: "https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb"
  },
  {
    id: 3,
    title: "Weekend Brunch",
    description: "Special brunch menu with bottomless mimosas",
    time: "Saturday & Sunday, 10:00 AM - 3:00 PM",
    image: "https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b"
  }
];

export const teamMembers = [
  {
    id: 1,
    name: "James Mitchell",
    role: "Executive Chef",
    image: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e",
    bio: "With over 15 years of culinary experience, James brings innovative flavors to every dish."
  },
  {
    id: 2,
    name: "Sarah Johnson",
    role: "Head Bartender",
    image: "https://images.unsplash.com/photo-1494790108755-2616b612b786",
    bio: "Sarah crafts our signature cocktails with passion and precision, creating memorable experiences."
  },
  {
    id: 3,
    name: "Michael Chen",
    role: "General Manager",
    image: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d",
    bio: "Michael ensures every guest receives exceptional service and attention to detail."
  }
];

export const testimonials = [
  {
    id: 1,
    name: "Emily Rodriguez",
    rating: 5,
    comment: "Absolutely incredible experience! The ambiance is perfect and the food is outstanding.",
    image: "https://images.unsplash.com/photo-1438761681033-6461ffad8d80"
  },
  {
    id: 2,
    name: "David Thompson",
    rating: 5,
    comment: "Best cocktails in town! The staff really knows their craft. Highly recommend.",
    image: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e"
  },
  {
    id: 3,
    name: "Lisa Wang",
    rating: 5,
    comment: "Perfect for date night. The atmosphere is romantic and the service is impeccable.",
    image: "https://images.unsplash.com/photo-1494790108755-2616b612b786"
  }
];