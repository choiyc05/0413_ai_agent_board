import React from 'react';
import './MainLayout.css';

const MainLayout = ({ children, bottomContent }) => {
  return (
    <div className="main-layout">
      {/* Top Section: Board/Content Area */}
      <section className="top-section">
        {children}
      </section>

      {/* Bottom Section: Chat Area */}
      <section className="bottom-section">
        {bottomContent}
      </section>
    </div>
  );
};

export default MainLayout;
