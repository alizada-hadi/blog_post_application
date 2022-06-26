import Navbar from './components/Navbar';
import { Provider } from 'react-redux'
import store from './store';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Home from './containers/Home';
import Login from './containers/Login';
import Register from './containers/Register';
import NotFound from './containers/404';


function App() {
  return (
    <Provider store={store}>

      <Router>
      <Navbar />
        <Routes>
          <Route path="/" exact element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />

          <Route path="*" element={<NotFound />} />
        </Routes>
      </Router>
    </Provider>
  );
}

export default App;
