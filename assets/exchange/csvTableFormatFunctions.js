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