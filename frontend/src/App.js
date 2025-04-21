import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Main from './pages/Main'; 
import Footer from './components/Footer';
import Header from './components/Header';
import MoviePage from './pages/MoviePage';  

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Routes>
          <Route path="/" element={<Main />} />
          <Route path="/movie/:id" element={<MoviePage />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;






/* import React from 'react';

import Main from './pages/Main';
import Footer from './components/Footer';
import Header from './components/Header';


function App() {
  return (
    <div className="App">
      <Header />
      <Main />
      <Footer />

    </div>
  );
}

export default App;
 */