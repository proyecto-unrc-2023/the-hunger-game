import React, { useState } from 'react';
import "./Login.css";

const Login = ({ onViewChange, onLogin, isLoggedIn }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [usernameError, setUsernameError] = useState('');
  const [passwordError, setPasswordError] = useState('');
  const [loginError, setLoginError] = useState(''); 
     
  const handleLogin = async () => {

    setUsernameError('');
    setPasswordError('');
    setLoginError('');

    if(!username) {
      setUsernameError('Nombre de usuario es obligatorio');
      return;
    }

    if (!password) {
      setPasswordError('Contraseña es obligatoria');
      return;
    }

    if (isLoggedIn) {
      setLoginError('No puedes iniciar otra sesión, desloguea primero.');
      return;
    }

    const userData = {
      name: username,
      password: password, 
    };

    try {
      const response = await fetch("http://localhost:5000/game/login", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
      });

      if (response.ok) {
        const responseData = await response.json();
        const accessToken = responseData.access_token; // se recupera el token de acceso
        localStorage.setItem('access_token', accessToken);

        onLogin(true);
        onViewChange('init');
      } else {
        setLoginError('Nombre de usuario o contraseña incorrectos');
      }
    } catch(error) {
      setLoginError('Error al iniciar sesión, intente nuevamente más tarde');
    }
  };

  const handleGoToInitGame = () => {
    onViewChange('init');
  };

  return (
    <div className="main-container">
      <div className="login-container">
        <div className="background"></div>
          <div className="login">
            <h2 className="custom-heading">Login</h2>
              <input
                type="text"
                placeholder="Username"
                value={username}
                onChange={(e) => {
                setUsername(e.target.value);
                setUsernameError('');
                setLoginError('');
                }}
              />
              {usernameError && <div className="error">{usernameError}</div>}
              <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => {
                setPassword(e.target.value);
                setPasswordError('');
                setLoginError('');
                }}
              />
              {passwordError && <div className="error">{passwordError}</div>}
              {loginError && <div clasName="error">{loginError}</div>}
              <button onClick={handleLogin}>Login</button>
              <button className="custom-button" onClick={handleGoToInitGame}>
                Back to menu
              </button>
          </div>
      </div>
    </div>
  );
};

export default Login;
