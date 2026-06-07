run_bibliometrix <- function(input_file, dbsource = "wos", format = "plaintext") {
  if (!requireNamespace("bibliometrix", quietly = TRUE)) {
    stop("Package 'bibliometrix' is required. Install with install.packages('bibliometrix').")
  }

  records <- bibliometrix::convert2df(
    file = input_file,
    dbsource = dbsource,
    format = format
  )
  bibliometrix::biblioAnalysis(records, sep = ";")
}

