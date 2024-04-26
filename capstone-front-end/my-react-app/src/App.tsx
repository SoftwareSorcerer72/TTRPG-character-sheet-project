// src/App.tsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import Login from './components/Login';
import SignUp from './components/SignUp';
import CharacterSheet from './components/CharacterSheet';
import EditUser from './components/EditUser';
import AddCharacterSheet from './components/AddCharacterSheet';
import NavBar from './components/NavBar';
import EditCharacterSheet from './components/EditCharacterSheet'; // import the EditCharacterSheet component

const App: React.FC = () => {
  return (
    <Router>
      <NavBar />
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/character-sheet/:id" element={<CharacterSheet />} />
        <Route path="/edit-character-sheet/:id" element={<EditCharacterSheet />} />
        <Route path="/edit-user" element={<EditUser />} />
        <Route path="/add-character-sheet" element={<AddCharacterSheet />} />
      </Routes>
    </Router>
  );
};

export default App;
