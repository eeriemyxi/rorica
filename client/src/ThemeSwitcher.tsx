import React, { useState, useEffect } from 'react';

const ThemeSwitcher = () => {
  const toggleTheme = () => {
    document.documentElement.classList.add("light");
  };

  return (
    <button onClick={toggleTheme}>Switch to Light Theme</button>
  );
};

export default ThemeSwitcher;
