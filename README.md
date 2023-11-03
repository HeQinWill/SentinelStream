# SentinelStream
With the closing of [Copernicus Open Access Hub](https://scihub.copernicus.eu/), previous accessing tools will soon be deprecated (e.g. [Sentinelsat](https://github.com/sentinelsat/sentinelsat)) due to the migration to [the Copernicus Data Space Ecosystem introduces new APIs](https://dataspace.copernicus.eu/news/2023-9-28-accessing-sentinel-mission-data-new-copernicus-data-space-ecosystem-apis). It's time to review and update my own data download workflow.

This app is a tool for searching and downloading datasets from the Sentinel satellite missions. It leverages [the new APIs](https://documentation.dataspace.copernicus.eu/APIs.html) from the Copernicus Data Space Ecosystem to provide users with a streamlined downloading experience.

The key features will include:
- Searching the catalog of datasets available from Sentinel for specific areas or dates
- Browsing search results and selecting the desired datasets to download
- Generating a download list with links of the chosen datasets to their local storage
- Allowing users to use their preferred downloading tools to fetch them easily from the download list
- Downloading Parallelly (multi-files and multi-process)
- Adding Network Proxy
- Showing Interface
