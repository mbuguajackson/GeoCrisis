import { useEffect, useRef } from "react";


async function loadMap(container) {
  const { initialize } = await import("../utils/map")
  return initialize(container)
}

const MapComponent = () => {
  const mapRef = useRef(null);

useEffect(() => {
    let cleanupFn

    if (mapRef.current) {
      loadMap(mapRef.current).then(({ cleanup, app, switchBasemap }) => {     

        cleanupFn = cleanup
     
      })
    }
    return () => {
      cleanupFn && cleanupFn()
        }
  }, [])

  return (
    <div style={{width:"100vw"}}>
      <div ref={mapRef} style={{ width: "100%", height: "100vh" }} />

    </div>
  );
};

export default MapComponent;
