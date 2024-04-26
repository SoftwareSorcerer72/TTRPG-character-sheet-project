import React, { useState } from 'react';
import { TextField, Button, Typography } from '@mui/material';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const SignUp: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [username, setUsername] = useState('');
  const navigate = useNavigate();

  const handleSignUp = async (event: React.FormEvent) => {
    event.preventDefault();
    try {
      await axios.post('http://localhost:5000/signup', { email, password, username });
      alert('Sign up successful');
      navigate('/login');
    } catch (error) {
      alert('Sign up failed');
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSignUp}>
      <Typography variant="h6">Sign Up</Typography>
      <TextField label="Username" fullWidth required value={username} onChange={e => setUsername(e.target.value)} />
      <TextField label="Email" type="email" fullWidth required value={email} onChange={e => setEmail(e.target.value)} />
      <TextField label="Password" type="password" fullWidth required value={password} onChange={e => setPassword(e.target.value)} />
      <Button type="submit" color="primary" variant="contained">Sign Up</Button>
    </form>
  );
};

export default SignUp;
