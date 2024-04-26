import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { AppBar, Toolbar, Typography, Button } from '@mui/material';

const NavBar: React.FC = () => {
  const navigate = useNavigate();
  const isLoggedIn = !!localStorage.getItem('token');

  const handleSignOut = () => {
    localStorage.removeItem('token'); // remove the token from local storage
    navigate('/login'); // redirect the user to the login page
  };

  return (
    <AppBar position="static" sx={{ backgroundColor: 'red' }}>
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          TTRPG Grimoire
        </Typography>
        {isLoggedIn ? (
          <>
            <Button color="inherit" component={Link} to="/">Dashboard</Button>
            <Button color="inherit" component={Link} to="/edit-user">Edit User</Button>
            <Button color="inherit" onClick={handleSignOut}>Sign Out</Button>
          </>
        ) : (
          <>
            <Button color="inherit" component={Link} to="/login">Log In</Button>
            <Button color="inherit" component={Link} to="/signup">Sign Up</Button>
          </>
        )}
      </Toolbar>
    </AppBar>
  );
};

export default NavBar;