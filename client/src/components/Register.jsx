// Register.js
import React, { useState } from 'react';
import './register.css';

const Register = ({ onViewChange }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [usernameError, setUsernameError] = useState('');
  const [passwordError, setPasswordError] = useState('');

  const handleRegister = async () => {
    setUsernameError('');
    setPasswordError('');

    if (!username) {
      setUsernameError('Nombre de usuario es obligatorio');
      return;
    }

    if (!password) {
      setPasswordError('Contraseña es obligatoria');
      return;
    }

    const userData = {
      name: username,
      password: password,
    };

    try {
      const response = await fetch("http://localhost:5000/game/register", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
      });

      if (response.ok) {
        console.log('Usuario registrado con éxito');
        onViewChange('init');
      } else {
        console.log('Fallo al registrar al Usuario');
        console.error('Error al registrar usuario');
      }
    } catch (error) {
      console.error('Error en la solicitud de registro', error);
    }
  };

  const handleGoToInitGame = () => {
    onViewChange('init');
  };

  return (
    <div className="main-container"> {/* Nueva línea */}
      <div className="register-container">
        <div className="background"></div>
        <div className="register">
          <h2 className="custom-heading">Registrarse</h2>
          <input
            type="text"
            placeholder="Nombre de usuario"
            value={username}
            onChange={(e) => {
              setUsername(e.target.value);
              setUsernameError('');
            }}
          />
          {usernameError && <div className="error">{usernameError}</div>}
          <input
            type="password"
            placeholder="Contraseña"
            value={password}
            onChange={(e) => {
              setPassword(e.target.value);
              setPasswordError('');
            }}
          />
          {passwordError && <div className="error">{passwordError}</div>}
          <button onClick={handleRegister}>Registrarse</button>
          <button className="custom-button" onClick={handleGoToInitGame}>
            Volver al menu
          </button>
        </div>
      </div>
    </div> 
  );
};

export default Register;
