"""
Class name
CamelCase

Python Fundamentals - 09 Classes

** All are public

Polymorphism - using objects of different types through a common interface
e.g. card printer - only need to know abstract details of interface : order

methods are called using instance.method()
- passing self instance to methord

Instance methods are functions defined inside the class
- should accept an object instance called self as the first parameter

late binding
inheritance is most useful for sharing implementation
"""


"""Model for aircraft flights"""


class Flight:
    """A flight with a particular passenger aircraft. """

    def __init__(self, number, aircraft): # initializer, not a constructor
        # f = Flight("BA758", Aircraft("G-EU", "Airbus A319, num_rows = 22, num_seats_per_row = 6))
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number  # avoid name clash, not directly call: covention to use _
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]
        # one wasted entry since python is 0 based [None]
        # {letter: None for letter in seats} one entry for each row in the aircraft
        # _ discard row number (not interested, = index)
        # [] list comprehension - distinch each dict obj to be created for each row
        """
        pp(f._seating)
        e.g. 3 rows, A,B,C seats
        [None,
        {'A':None, 'B':None,'C':None}
        {'A':None, 'B':None,'C':None}
        {'A':None, 'B':None,'C':None}
        ]
        
        """

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def _parse_seat(self, seat):  #_ for implementation detail
        """Parse a seat designator into a valid row and letter.

        Args:
            seat: A seat designator such as 12F

        Returns:
            A tuple containing an integer and a string for row and seat.
        """
        row_numbers, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))

        if row not in row_numbers:
            raise ValueError("Invalid row number {}".format(row))

        return row, letter

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger.

        Args:
            seat: A seat designator such as '12C' or '21F'.
            passenger: The passenger name.

        Raises:
            ValueError: If the seat is unavailable.
        """
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))

        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        """Relocate a passenger to a different seat.

        Args:
            from_seat: The existing seat designator for the
                       passenger to be moved.

            to_seat: The new seat designator.
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to relocate in seat {}".format(from_seat))

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} already occupied".format(to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        """An iterable series of passenger seating allocations."""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row, letter))  # generator function, yielding passager as found


class Aircraft: #base class

    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class AirbusA319(Aircraft):

    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"


class Boeing777(Aircraft):

    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        # For simplicity's sake, we ignore complex
        # return (range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row])
        # a = Aircraft("G-EU", "Airbus A319, num_rows = 22, num_seats_per_row = 6)
        # run a. registration(), model(), seating_plan() : (range(1,23),'ABCDEF')
        # seating arrangement for first-class
        return range(1, 56), "ABCDEGHJK"


def make_flights():
    # from airtravel import make_flight, f=make_flight, f.num_available_seats()
    f = Flight("BA758", AirbusA319("G-EUPT"))
    f.allocate_seat('12A', 'Guido van Rossum')
    f.allocate_seat('15F', 'Bjarne Stroustrup')
    f.allocate_seat('15E', 'Anders Hejlsberg')
    f.allocate_seat('1C', 'John McCarthy')
    f.allocate_seat('1D', 'Richard Hickey')

    g = Flight("AF72", Boeing777("F-GSPS"))
    g.allocate_seat('55K', 'Larry Wall')
    g.allocate_seat('33G', 'Yukihiro Matsumoto')
    g.allocate_seat('4B', 'Brian Kernighan')
    g.allocate_seat('4A', 'Dennis Ritchie')

    return f, g


def console_card_printer(passenger, seat, flight_number, aircraft):
    # break long lines without line breaks
    output = "| Name: {0}"     \   
             "  Flight: {1}"   \
             "  Seat: {2}"     \
             "  Aircraft: {3}" \
             " |".format(passenger, flight_number, seat, aircraft)
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()
