---
layout: page
title: Full Table
permalink: /full-table/
---
<html lang="en">

<style>
.myDiv {
    overflow: scroll;
    overflow-x: scroll;
    overflow-y: scroll;
}
</style>

<head>
    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1, shrink-to-fit=yes" name="viewport">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

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
<script src="../assets/js/jquery.csv.min.js"></script>
<script src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.datatables.net/1.10.19/js/dataTables.bootstrap4.min.js"></script>
<script src="../assets/js/csv_to_html_table.js"></script>
<script>
	function format_image(link) {
		if (link){
			position = link.search("id=");
			hash = link.substring(position+3,link.length);
			finalLink = "https://drive.google.com/thumbnail?id=" + hash;
            return "<a href='" + finalLink + "'> <img src='" + finalLink + "'> </a>";
		}
		else return "";
	}
    function format_link(link) {
        if (link)
            return "<a href='" + link + "' target='_blank'>link</a>";
        else return "";
    }
    function remove(element) {
    	return "";
    }
    function atAndDotReplacement(string) {
    	newString = string.replace("@", "\n_at_");
    	newString = newString.replace(".", "_dot_");
    	return newString
    }

    CsvToHtmlTable.init({
        csv_path: "../assets/nimeTest.csv",
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
        	[7, atAndDotReplacement],
        ]
    });
</script>
</body>

</html>

