import React, { useRef, useEffect } from "react";
import MapView from "@arcgis/core/views/MapView";
import Map from "@arcgis/core/Map";
import "@arcgis/core/assets/esri/themes/light/main.css";

const MapComponent = () => {
  const mapRef = useRef(null);

  useEffect(() => {
    if (!mapRef.current) return;

    const webmap = new Map({
      basemap: "satellite" // Changed to a more common basemap
    });

    const view = new MapView({
      container: mapRef.current,
      map: webmap,
      center: [36.8219, -1.2921], // Nairobi coordinates
      zoom: 10, // Using zoom instead of scale for better control
      padding: { top: 10 } // Add some padding from the top
    });

    // Handle window resize
    const handleResize = () => {
      view && view.extent && view.extent && view.goTo(view.extent);
    };
    window.addEventListener('resize', handleResize);

    // Cleanup
    return () => {
      if (view) {
        view.container = null;
        view.destroy();
      }
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  return (
    <div 
      ref={mapRef} 
      style={{
        width: '100%',
        height: '100vh',
        padding: 0,
        margin: 0
      }}
    />
  );
};

export default MapComponent;