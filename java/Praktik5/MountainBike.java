package Praktik5;
class MountainBike extends Bicycle {
    public int seatHeight;

    public MountainBike(int gear, int speed, int starHeight)
    {
        super(gear, speed);
        seatHeight = starHeight;
    }

    public void setHeight(int newValue)
    {
        seatHeight = newValue;
    }

    @Override public String toString()
    {
        return (super.toString() + "\nseat height is" + seatHeight);
    }
}
