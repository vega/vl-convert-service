# vl-convert-service

# Local development

```
vercel dev
```

This will launch service on http://localhost:3000

# Local testing

First, start the development server. Then run tests with:

```bash
pipenv run pytest -s tests
```

# POST

Convert Vega-Lite to Vega using version 4.17 of the Vega-Lite JavaScript library
```bash
curl -X POST "https://vl-convert-service-hi83yf5kw-jonmmease.vercel.app/api/vl2vg?vl_version=4.17" \
     -d '{"$schema": "https://vega.github.io/schema/vega-lite/v5.json", "data": {"url": "https://raw.githubusercontent.com/vega/vega-datasets/next/data/movies.json"}, "mark": "circle", "encoding": {"x": {"bin": {"maxbins": 10}, "field": "IMDB Rating"}, "y": {"bin": {"maxbins": 10}, "field": "Rotten Tomatoes Rating"}, "size": {"aggregate": "count"}}}'
     -o chart.vg.json
```

Convert Vega-Lite to SVG with the latest version of Vega-Lite
```bash
curl -X POST "https://vl-convert-service-bdpam60xo-jonmmease.vercel.app/api/vl2svg" \
     -d '{"$schema": "https://vega.github.io/schema/vega-lite/v5.json", "data": {"url": "https://raw.githubusercontent.com/vega/vega-datasets/next/data/movies.json"}, "mark": "circle", "encoding": {"x": {"bin": {"maxbins": 10}, "field": "IMDB Rating"}, "y": {"bin": {"maxbins": 10}, "field": "Rotten Tomatoes Rating"}, "size": {"aggregate": "count"}}}' \
     -o chart.svg
```

Convert Vega-Lite to PNG with the latest version of Vega-Lite and image scale factor of 3
```bash
curl -X POST "https://vl-convert-service-d1s61my0q-jonmmease.vercel.app/api/vl2png?scale=3" \
     -d '{"$schema": "https://vega.github.io/schema/vega-lite/v5.json", "data": {"url": "data/movies.json"}, "mark": "circle", "encoding": {"x": {"bin": {"maxbins": 10}, "field": "IMDB Rating"}, "y": {"bin": {"maxbins": 10}, "field": "Rotten Tomatoes Rating"}, "size": {"aggregate": "count"}}}' \
     -o chart.png  
```

Convert Vega-Lite to PDF with the latest version of Vega-Lite
```bash
curl -X POST "https://vl-convert-service-hgj3d4xfc-jonmmease.vercel.app/api/vl2pdf" \
     -d '{"$schema": "https://vega.github.io/schema/vega-lite/v5.json", "data": {"url": "https://raw.githubusercontent.com/vega/vega-datasets/next/data/movies.json"}, "mark": "circle", "encoding": {"x": {"bin": {"maxbins": 10}, "field": "IMDB Rating"}, "y": {"bin": {"maxbins": 10}, "field": "Rotten Tomatoes Rating"}, "size": {"aggregate": "count"}}}' \
     -o chart2.pdf
```


```bash
curl -X POST "https://vl-convert-service-o0ouzbt2r-jonmmease.vercel.app/api/vl2pdf" \
     -d '{"$schema": "https://vega.github.io/schema/vega-lite/v5.json", "data": {"url": "https://raw.githubusercontent.com/vega/vega-datasets/next/data/barley.json"}, "mark": "bar", "encoding": {"x": {"aggregate": "sum", "field": "yield"}, "y": {"field": "variety"}, "color": {"field": "site"}}, "title": "Figure Title", "config": {"axis": {"labelFont": "monospace", "titleFont": "serif"}, "legend": {"labelFont": "sans-serif", "titleFont": "serif"}, "title": {"font": "Impact"}}}' \
     -o chart_bar.pdf
```

```bash
curl -X POST "https://vl-convert-service-o0ouzbt2r-jonmmease.vercel.app/api/vl2png" \
     -d '{"$schema": "https://vega.github.io/schema/vega-lite/v5.json", "data": {"url": "https://raw.githubusercontent.com/vega/vega-datasets/next/data/barley.json"}, "mark": "bar", "encoding": {"x": {"aggregate": "sum", "field": "yield"}, "y": {"field": "variety"}, "color": {"field": "site"}}, "title": "Figure Title", "config": {"axis": {"labelFont": "monospace", "titleFont": "serif"}, "legend": {"labelFont": "sans-serif", "titleFont": "serif"}, "title": {"font": "Impact"}}}' \
     -o chart_bar.png
```

```bash
curl -X POST "https://vl-convert-service-o0ouzbt2r-jonmmease.vercel.app/api/vl2png" \
     -d '{"$schema": "https://vega.github.io/schema/vega-lite/v5.json", "data": {"url": "https://raw.githubusercontent.com/vega/vega-datasets/next/data/barley.json"}, "mark": "bar", "encoding": {"x": {"aggregate": "sum", "field": "yield"}, "y": {"field": "variety"}, "color": {"field": "site"}}, "title": "Figure Title", "config": {"axis": {"labelFont": "Liberation Mono", "titleFont": "serif"}, "legend": {"labelFont": "sans-serif", "titleFont": "serif"}, "title": {"font": "Impact"}}}' \
     -o chart_bar.png
```

```bash
curl -X POST "https://vl-convert-service-o0ouzbt2r-jonmmease.vercel.app/api/vl2png" \
     -d '{"$schema": "https://vega.github.io/schema/vega-lite/v5.json", "data": {"url": "https://raw.githubusercontent.com/vega/vega-datasets/next/data/barley.json"}, "mark": "bar", "encoding": {"x": {"aggregate": "sum", "field": "yield"}, "y": {"field": "variety"}, "color": {"field": "site"}}, "title": "Figure Title", "config": {"axis": {"labelFont": "monospace", "titleFont": "serif"}, "legend": {"labelFont": "sans-serif", "titleFont": "serif"}, "title": {"font": "Impact"}}}' \
     -o chart_bar.png
```