---
layout: page
title: Exchange Full Table
permalink: /exchange-full-table/
---

<style>
.myDiv {
    overflow: scroll;
    overflow-x: scroll;
    overflow-y: scroll;
}
</style>

<head>
    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS"
        crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.datatables.net/1.10.19/css/dataTables.bootstrap4.min.css">
</head>

<body>
<div class="container-fluid">
    <main class="row">
        <div class="myDiv" id="table-container"></div>
    </main>
</div>

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
    function format_link(link) {
        if (link)
            return "<a href='" + link + "' target='_blank'>link</a>";
        else return "";
    }
    function format_wider(text) {
        text += " ____________________________________";
        return text;
    }

    CsvToHtmlTable.init({
        csv_path: "../assets/exchange/exchange-table.csv",
        element: "table-container",
        allow_download: false,
        csv_options: {
            separator: ",",
            delimiter: '"'
        },
        datatables_options: {

        },
        custom_formatting: [
            [2, format_link],
        	[3, format_link],
        	[4, format_image],
        	[5, format_link],
            [13, format_link]
        ]
    });
</script>
</body>

</html>

