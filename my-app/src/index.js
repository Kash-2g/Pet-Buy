import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals'
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import Home from './Componets/Homepage';
import Breeds from './Componets/Breeds';


import Buy from './Componets/Buy';




const root = ReactDOM.createRoot(document.getElementById('root'));
const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
  },
  
  {
    path: '/home',
    element: <Home />,
  },
 
  {
    path: '/breeds',
    element: <Breeds />,
  },
  {
    path: '/Buy',
    element: <Buy />,
  },

  
])
root.render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode>
);




// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();