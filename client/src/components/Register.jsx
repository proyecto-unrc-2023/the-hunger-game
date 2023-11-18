import React, { useState } from 'react';
import './Register.css';

const Register = ({ onViewChange }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [usernameError, setUsernameError] = useState('');
  const [passwordError, setPasswordError] = useState('');
  const [confirmPasswordError, setConfirmPasswordError] = useState('');
  const [registerError, setRegisterError] = useState('');

  const handleRegister = async () => {
    setUsernameError('');
    setPasswordError('');
    setRegisterError('');

    if (!username) {
      setUsernameError('Nombre de usuario es obligatorio');
      return;
    }

    if (!password) {
      setPasswordError('Contraseña es obligatoria');
      return;
    }

    if (password !== confirmPassword) {
      setConfirmPasswordError('Las contraseñas no coinciden');
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
        onViewChange('init');
      } else {
        setRegisterError('Nombre de usuario no disponible');
      }
    } catch (error) {
      setRegisterError('Error al registrarse, intente nuevamente más tarde');
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
          <input
            type="password"
            placeholder="Confirmar contraseña"
            value={confirmPassword}
            onChange={(e) => {
              setConfirmPassword(e.target.value);
              setConfirmPasswordError('');
            }}
          />
          {confirmPasswordError && <div className="error">{confirmPasswordError}</div>}  
          {registerError && <div clasName="error">{registerError}</div>}
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
