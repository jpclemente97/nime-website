---
layout: page
title: Exchange
permalink: /exchange/
---





To date, hundreds of NIMEs have been built and presented during the annual conference (and in other academic/artistic venues). Thereafter, their fate is mostly unknown. Do they still exist? Are they still in full/partial working condition? Are they available for use by other researchers or artists? We believe that several of the presented NIMEs still exist and are just collecting dust in our storage. Making existing NIMEs available to others can have mutual benefits. This also resonates with trends that have emerged in recent years in the NIME community: sustainable and eco-friendly research, longevity of NIMEs, reuse or redesign of old NIMEs, diversity and inclusion.

The goal of this initiative is to develop a framework to facilitate the use of existing NIME by other researchers and/or artists. This may include:

- Structure and hosting of a database of existing NIME (e.g. what information to include), populated and maintained by the community (how to promote this?).
- Guidelines and practicalities related to the exchange of NIMEs (e.g. exchanging
the hardware during the annual conference, visiting when the hardware can not be moved, etc.)

If you want to add your NIME to the Exchange list, please fill up this [form](https://docs.google.com/forms/d/e/1FAIpQLSfcWRfPuj4KBqp3WplTrtnX636scaNdMWUZLBeddRCKWAErMw/viewform?usp=sf_link)



<br>

[View full table](/full-table/)



<head>
    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS"
        crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.datatables.net/1.10.19/css/dataTables.bootstrap4.min.css">
</head>

<div id="table-container"></div>

<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.2.1/js/bootstrap.bundle.min.js"></script>
<script src="../assets/exchange/jquery.csv.min.js"></script>
<script src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.datatables.net/1.10.19/js/dataTables.bootstrap4.min.js"></script>
<script src="../assets/exchange/csv-to-html-table.js"></script>
<script>
	function format_image(link) {
		if (link){
			position = link.search("id=");
			hash = link.substring(position+3,link.length);
			ThumbLink = "https://drive.google.com/thumbnail?id=" + hash;
            DirectLink = "https://drive.google.com/uc?id=" + hash;
            return "<a href='" + DirectLink + "'> <img src='" + ThumbLink + "'> </a>";
		}
		else return "";
	}

    CsvToHtmlTable.init({
        csv_path: "../assets/exchange/exchange-table-small.csv",
        element: "table-container",
        allow_download: false,
        csv_options: {
            separator: ",",
            delimiter: '"'
        },
        datatables_options: {
            paging: false,
            scrollY: true,
            fixedHeader: false,
            lengthChange: true,
            autoWidth: false

        },
        custom_formatting: [
        	[2, format_image]
        ]
    });
</script>


