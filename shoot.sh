for wh in 360x740 390x844 430x932 1440x900; do w=${wh%x*}; h=${wh#*x}; for y in 0 300; do
 google-chrome --headless=new --no-sandbox --hide-scrollbars --window-size=$w,$h --virtual-time-budget=3000 --screenshot=shots/fix-$wh-$([ $y = 0 ] && echo top || echo scroll300).png "http://localhost:8766/#y$y" 2>/dev/null; done; done
