# Parking-reservation-API


> API for booking
```bash
curl 127.0.0.1:8080/book/<BAY NO.(1-4)>/<NAME>/<DATE(DD:MM:YYYY)>
```

> API for for admin to watch all bookings
```bash
curl 127.0.0.1:8080/dev
```
> API data structure: { DATE: {  SPOT: { "name" : NAME }  }  }

## Examples

- Alice, Bob, Charlie and Dave book a parking bay for 1st June 2022
```bash
curl 127.0.0.1:8080/book/1/Alice/01:06:2022
 # Output: Congrats! Alice, your reserved bay no. 1 on 01/06/2022

curl 127.0.0.1:8080/book/2/Bob/01:06:2022
 # Output: Congrats! Bob, your reserved bay no. 2 on 01/06/2022

curl 127.0.0.1:8080/book/3/Charlie/01:06:2022
 # Output: Congrats! Charlie, your reserved bay no. 3 on 01/06/2022

curl 127.0.0.1:8080/book/4/Dave/01:06:2022
 # Output: Congrats! Dave, your reserved bay no. 4 on 01/06/2022
```

- Ed tried to book a parking bay on the same day but is unable to because there are no free days.
```bash
curl 127.0.0.1:8080/book/4/Ed/01:06:2022 
# Output: Ed on 01:06:2022 bay 4 is already booked by someone 
```

- Ed books a parking bay for 2nd June 2022
```bash
curl 127.0.0.1:8080/book/1/Ed/02:06:2022
# Output: Congrats! Ed, your reserved bay no. 1 on 02/06/2022 
```

- Querying bookings for 1st June 2022 returns 4 bookings with the allocated bay and each customer’s details.
```bash
curl 127.0.0.1:8080/dev/01:06:2022
# Output: {"1":{"name":"Alice"},"2":{"name":"Bob"},"3":{"name":"Charlie"},"4":{"name":"Dave"}}
