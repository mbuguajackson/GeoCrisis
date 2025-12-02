import ArcGISMap from "@arcgis/core/Map"
import FeatureLayer from "@arcgis/core/layers/FeatureLayer"
import MapView from "@arcgis/core/views/MapView"
import { watch } from "@arcgis/core/core/reactiveUtils"
import SimpleRenderer from "@arcgis/core/renderers/SimpleRenderer"
import SimpleMarkerSymbol from "@arcgis/core/symbols/SimpleMarkerSymbol"
import Editor from "@arcgis/core/widgets/Editor"



const app = {}

let handler

export async function initialize(container) {
  // 0. Destroy previous view if initialize is called
  if (app.view) {
    app.view.destroy()
  }


  const polesLayer = new FeatureLayer({
    url: "https://services6.arcgis.com/uEViOZnjj4wj8FP7/arcgis/rest/services/poles/FeatureServer/0",
  
  })

  const transformersLayer = new FeatureLayer({
    url: "https://services6.arcgis.com/uEViOZnjj4wj8FP7/arcgis/rest/services/transformers/FeatureServer/0",
  
  })

  const linesLayer = new FeatureLayer({
    url: "https://services6.arcgis.com/uEViOZnjj4wj8FP7/arcgis/rest/services/features/FeatureServer/2",
  })

  // 2. Create a map
  const map = new ArcGISMap({
    basemap: "streets-dark-3d",
    layers: [polesLayer, transformersLayer, linesLayer],
  })

  // 3. Create a view. View = Map + Container (div)
  const view = new MapView({
    map,
    container,
    zoom: 10,
    center: [36.817223, -1.286389],
  })


  // 4. Watch for changes in state
  handler = watch(
    () => view.stationary && view.extent,
    () => {
      app.savedExtent = view.extent.toJSON()
    }
  )

  // Additional stuff

  app.map = map
//   app.layers = { polesLayer, transformersLayer, linesLayer }
  app.view = view


  return {
    cleanup,
    app,
    switchBasemap,
  }
}

function cleanup() {
  // 1. Detach watcher
  handler?.remove()

  // 2. Destroy view
  app.view?.destroy()
}

export function switchBasemap(name) {
  if (!app.map) return
  app.map.basemap = name
}