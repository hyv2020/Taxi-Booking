# Taxi-Booking
A python program to mimic taxi booking.

This is the version 2 of the taxi booking program, it is not completed. It has some data validations but the generation of booking number hasn't been tested. Currently it doesn't read or write database and it doesn't have a GUI.

Planning to add a read function to load data from 3 csv files and overwrite them as the database updates.

There are some dummy data in the current build:

There is a dummy customer with id: "0", name: "Demo", address: "Demo address", email: "a", password: "a", phone: "12341234123", card number: "1234123412341234".

Two dummy taxi driver: TaxiDriver 1 has id: "0", name: "Demo driver", plate number: "ABC 123", password: "1234".

TaxiDriver 2 has id: "1", name: "Demo driver 2", plate number: "ABC 456", password: "1234".

Two dummy booking: Booking 1 details: Customer 1, Taxi driver 1, id: "0", time: "9.00am", date: "01/01/2021", drop off address: "Demo address 2".

Booking 2: Customer 1, Taxi driver 2, id: "1", time: "9.00am", date: "01/01/2021", drop off address: "Demo address 3".
