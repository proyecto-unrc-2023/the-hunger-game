import React from 'react';
import "./Logout.css";

const Logout = ({ isLoggedIn, setIsLoggedIn, onViewChange }) => {
  
  const handleLogout = async () => {
    try {
      const accessToken = localStorage.getItem('access_token');
      
      if (!accessToken) {
        console.error('Token de acceso no encontrado al cerrar sesión.')
        return;
      }

      const response = await fetch('http://localhost:5000/game/logout', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${accessToken}`
        },
      });

      if (response.ok) {
        localStorage.removeItem('access_token');
        setIsLoggedIn(false);
        onViewChange('init');
      } else {
        console.error('Error al cerrar sesión:', response.status);
      }
    } catch (error) {
      console.error('Error al cerrar sesión:', error);
    }
  };

  return (
    <button className='logout' onClick={handleLogout} disabled={!isLoggedIn}>
      LOGOUT
    </button>
  );
};

export default Logout;
