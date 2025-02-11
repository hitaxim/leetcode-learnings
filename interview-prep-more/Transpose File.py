awk '{ for(i = 1 ; i <= NF ; i++) {
        if (!column[i]) { column[i] = $i }
        else { column[i] = column[i]" "$i }
    } }
    END { for(i=1; i<=length(column); i++) print column[i] }' file.txt
