import React from 'react';

const Logout = ({ isLoggedIn, setIsLoggedIn, onViewChange }) => {
  const handleLogout = async () => {
    try {
      const accessToken = localStorage.getItem('access_token');
      
      if (!accessToken) { // manejo de error si no hay un token de acceso
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
        localStorage.removeItem('access_token'); // borra el token al cerrar la sesion
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
    <button onClick={handleLogout} disabled={!isLoggedIn}>
      Cerrar sesión
    </button>
  );
};

export default Logout;
