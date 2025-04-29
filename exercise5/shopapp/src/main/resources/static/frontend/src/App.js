import React, { useState } from 'react';
import Products from './Products';
import Payments from './Payments';

function App() {
  const [selectedProduct, setSelectedProduct] = useState(null);

  return (
      <div className="App">
        <Products onSelect={setSelectedProduct} />
        <Payments selectedProduct={selectedProduct} />
      </div>
  );
}

export default App;
