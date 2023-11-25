import React, { useState } from 'react';
import './Register.css';

const Register = ({ onViewChange, isLoggedIn }) => {
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
      setUsernameError('Username is required');
      return;
    }

    if (!password) {
      setPasswordError('Password is required');
      return;
    }

    if (password !== confirmPassword) {
      setConfirmPasswordError('Passwords do not match');
      return;
    }

    if (isLoggedIn) {
      setRegisterError('You can not register, you must logout first');
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
        setRegisterError('Username taken');
      }
    } catch (error) {
      setRegisterError('Error registering, please try again more later');
    }
  };

  const handleGoToInitGame = () => {
    onViewChange('init');
  };

  return (
    <div className="main-container">
      <div className="register-container">
        <div className="background"></div>
        <div className="register">
          <h2 className="custom-heading">Register</h2>
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => {
              setUsername(e.target.value);
              setUsernameError('');
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
            }}
          />
          {passwordError && <div className="error">{passwordError}</div>}
          <input
            type="password"
            placeholder="Confirm password"
            value={confirmPassword}
            onChange={(e) => {
              setConfirmPassword(e.target.value);
              setConfirmPasswordError('');
            }}
          />
          {confirmPasswordError && <div className="error">{confirmPasswordError}</div>}  
          {registerError && <div clasName="error">{registerError}</div>}
          <button onClick={handleRegister}>Register</button>
          <button className="custom-button" onClick={handleGoToInitGame}>
            Back to menu
          </button>
        </div>
      </div>
    </div> 
  );
};

export default Register;
