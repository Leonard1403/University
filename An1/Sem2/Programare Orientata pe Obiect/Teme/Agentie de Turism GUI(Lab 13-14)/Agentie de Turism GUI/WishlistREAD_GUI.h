#include "observer.h"
#include "Service.h"
#include "Wishlist.h"
#include <qwidget.h>
#include <qpainter.h>
#include <random>
#include <cmath>

#define RECTANGLE_MAX_DIM 256

class WishlistReadOnlyGUI :public QWidget, public Observer {
private:
	Wishlist& wishlist;

public:
	WishlistReadOnlyGUI(Wishlist& wishlist);

	void update() override;

	void paintEvent(QPaintEvent* event) override;

	~WishlistReadOnlyGUI() {
		this->wishlist.removeObserver(this);
	}
};