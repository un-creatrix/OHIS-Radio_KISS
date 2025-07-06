========================
Usage of OHIS Radio KISS
========================
What is the **OHIS Radio KISS Adapter**?

It is an adapter intended to bring any radio no matter its wiring standard or level from a Professional, Ham, DIY, Cheap Chinese, or Crystal with a Wire Hanging out of It; to be compatible with the OHIS connection Std. with very little to no effort other than looking up your radios needed connections and connecting said wires to the OHIS Radio KISS.

------------
Installation
------------

Usage
-----

Wiring
------

---------------
Board Features
---------------

Accessory Connection Pins
-------------------------

**(JP1) Pin Group #1** - OHIS Connection Nets

+---+------------------------+----+-------------------------+
|PIN| Connection Net         | PIN| Connection Net          |
+===+========================+====+=========================+
| 1 | OHIS Headphone Left    |  6 | OHIS Microphone Ground  |
+---+------------------------+----+-------------------------+
| 2 | OHIS Headphone Right   |  7 | OHIS PTT (Gnd Trig.)    |
+---+------------------------+----+-------------------------+
| 3 | Ground                 |  8 | Accessory  5v 500ma (+) |
+---+------------------------+----+-------------------------+
| 4 | OHIS Headphone Ground  |  9 | OHIS 5v (+)             |
+---+------------------------+----+-------------------------+
| 5 | OHIS Microphone Line   | 10 | OHIS 5v (-)             |
+---+------------------------+----+-------------------------+
\ :sup:`*` Pin **9/JP1** is a dedicated power connection supplying 500ma on a resettable fuse for accessories any 5v (-) maybe used in conjunction with this point.

**(JP2) Pin Group #2** - Radio Connection, Unregulated Power, and Accessory Indicator Light

+----+--------------------------+----+----------------------------+
| PIN| Connection Net           | PIN| Connection Net             |
+====+==========================+====+============================+
|  1 | Radio Headphone Left     |  6 | Radio Microphone Ground    |
+----+--------------------------+----+----------------------------+
|  2 | Radio Headphone Right    |  7 | Radio PTT Enable           |
+----+--------------------------+----+----------------------------+
|  3 | Accessory Indicator LED   |  8 | Radio PTT Ground          |
+----+--------------------------+----+----------------------------+
|  4 | Radio Headphone Ground   |  9 | Unregulated Voltage In (+) |
+----+--------------------------+----+----------------------------+
|  5 | Radio Microphone Line    | 10 | Unregulated Voltage In (+) |
+----+--------------------------+----+----------------------------+
\ :sup:`*` Pin **3/JP2** offers access to a dedicated indicator LED for accessory boards to give the opportunity of a uniform look between different accessory boards being used.

Modification Points
-------------------

Breakable Points which are Either Cuttable/Solderable SMT traces or Removable 0Ω Resistors

+-----+-------------------------------------------------+
| CID | Connected Net #1 & Connected Net #2             |
+=====+=================================================+
| JP3 | OHIS (-) to 5v Reg (-)                          |
+-----+-------------------------------------------------+
| R11 | Radio Headphone L to OHIS Headphone L           |
+-----+-------------------------------------------------+
| R12 | Radio Headphone R to OHIS Headphone R           |
+-----+-------------------------------------------------+
| R13 | Radio Headphone GND to OHIS Headphone GND       |
+-----+-------------------------------------------------+
| R14 | Radio Mic Line to (0/-20)db Pad "OHIS Mic Line" |
+-----+-------------------------------------------------+
| R15 | Radio Mic GND to OHIS Mic GND                   |
+-----+-------------------------------------------------+
| R16 | PTT SSR Isolator Anode to 5v Reg (+)            |
+-----+-------------------------------------------------+
| R17 | PTT SSR Isolator Cathode to OHIS PTT GND        |
+-----+-------------------------------------------------+
