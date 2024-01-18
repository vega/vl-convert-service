# vl-convert-service
This project defines a REST API to [VlConvert](https://github.com/vega/vl-convert) hosted on Vercel at https://vl-convert-service.vercel.app.

# Endpoints
The following endpoints are available

## `vl_version` Query parameter
All the endpoints that accept a Vega-Lite specification support a query parameter named `vl_version`, which defines the version of the Vega-Lite library that should be used. See [VlConvert Release Notes](https://github.com/vega/vl-convert/releases/) for info on the supported versions. Defaults to the latest Vega-Lite version.

## GET `/api/version`
Retrieve the version of VlConvert that is backing the API

## POST `/api/vl2vg`
Compile a Vega-Lite spec to a Vega spec. The Vega-Lite spec should be provided as the request body. The following optional query parameters are supported:
 - `vl_version`: The Vega-Lite version.

## POST `/api/vl2svg`
Convert a Vega-Lite spec to an SVG image. The Vega-Lite spec should be provided as the request body. The following optional query parameters are supported:
 - `vl_version`: The Vega-Lite version.
 - `theme`: Named theme as supported by [vega-themes](https://github.com/vega/vega-themes).

## POST `/api/vl2png`
Convert a Vega-Lite spec to a PNG image. The Vega-Lite spec should be provided as the request body. The following optional query parameters are supported:
 - `vl_version`: The Vega-Lite version.
 - `theme`: Named theme as supported by [vega-themes](https://github.com/vega/vega-themes).
 - `scale`: Scale factor for the resulting image size. Defaults to 1.
 - `ppi`: Pixel's per inch of the resulting image. Defaults to 72.

## POST `/api/vl2pdf`
Convert a Vega-Lite spec to a PDF document. The Vega-Lite spec should be provided as the request body. The following optional query parameters are supported:
 - `vl_version`: The Vega-Lite version.
 - `theme`: Named theme as supported by [vega-themes](https://github.com/vega/vega-themes).
 - `scale`: Scale factor for the resulting image size. Defaults to 1.
 
## POST `/api/vg2svg`
Convert a Vega spec to an SVG image. The Vega spec should be provided as the request body..

## POST `/api/vg2png`
Convert a Vega spec to a PNG image. The Vega spec should be provided as the request body. The following optional query parameters are supported:
 - `scale`: Scale factor for the resulting image size. Defaults to 1.
 - `ppi`: Pixel's per inch of the resulting image. Defaults to 72.

## POST `/api/vg2pdf`
Convert a Vega spec to a PDF document. The Vega spec should be provided as the request body. The following optional query parameters are supported:
 - `scale`: Scale factor for the resulting image size. Defaults to 1.
 
## Curl usage
Here is an example of converting a Vega-Lite spec to a PNG image using curl. A 2.0 scale factor and dark theme are specified as query parameters.

```bash
curl -X POST "https://vl-convert-service.vercel.app/api/vl2png?scale=2.0&theme=dark" \
     -d '{"$schema": "https://vega.github.io/schema/vega-lite/v5.json", "data": {"url": "data/movies.json"}, "mark": "circle", "encoding": {"x": {"bin": {"maxbins": 10}, "field": "IMDB Rating"}, "y": {"bin": {"maxbins": 10}, "field": "Rotten Tomatoes Rating"}, "size": {"aggregate": "count"}}}' \
     -o chart.png  
```

# Development
The REST API can be server locally using the [Vercel CLI](https://vercel.com/docs/cli)
```
vercel dev
```

This will launch service on http://localhost:3000

## Running tests

After starting the development server, tests may can be run with:

```bash
pipenv run pytest -s tests
```

Always run tests locally before pushing changes

## Updating vl-convert
Update the version of vl-convert-python in `Pipfile`, the run:

```
pipenv lock
```
