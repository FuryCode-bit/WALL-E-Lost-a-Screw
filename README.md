<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/FuryCode-bit/WALL-E-Lost-a-Screw">
    <img src="readme/fe.png" alt="Logo" height="80">
  </a>

  <h3 align="center"></h3>
    Fabrica
  <p align="center">
    Projeto Inteligencia Artificial 2023/2024
    <br />
    <a href="https://github.com/FuryCode-bit/WALL-E-Lost-a-Screw"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/FuryCode-bit/WALL-E-Lost-a-Screw)

In this project we will create the AI for a robot that moves under our control in a
virtual world, that corresponds to a factory.

In the middle right we have the factory entrance, where the robot always starts.
Next to it we see a battery charger that can be used by the robot, when necessary.
On the bottom right corner we see the battery status (currently is 90) and the
coordinates of the robot position (x = 565 and y = 400).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To run the code we just need to write python3 ia.py in a terminal. To control the robot you use the following keys: W=up, S=down, A=left, D=right, ESC=end. While moving around, the robot is going to find several objects, and when it comes close enough to them, their names and category (see below) is given to the function work() that receives information regarding the robot’s localization, its
battery status and the list of nearby objects.

### Prerequisites

* Install Libraries 
  ```sh
  pip3 install pygame networkx numpy scipy scikit-learn pyAgrum
  ```

* Run code
  ```sh
  python3 ia.py
  ```
<!-- How the world works -->
### How the world works

The robot always starts in the same location (zone 10, the factory entrance). The battery is discharging as time goes by, and when it reaches zero charge, the simulation finishes. The battery can be recharged by touching the two chargers that exist in the factory.

At any moment, the number of the zone where the robot is can be obtained using the coordinates of its position and the information from the figure.

The S represents supervisor, the V represents visitor, the Z represents a Zone and the O represents a worker (Operário in Portuguese). Note that the numbers from 1 to 4 are assigned to corridors. In this figure the corridor limits are marked with blue lines.

The workers are normally around machines. The supervisors want to evaluate how the workers behave, specially when they are operating the machines. There may be some people visiting the factory, the visitors, which are normally accompanied by a supervisor. The next table shows the probabilities relating these elements, that can be used to answer some questions:

<table>
  <thead>
    <tr>
      <th>Machine</th>
      <th>Worker</th>
      <th>P(Supervisor | Machine, Worker)</th>
    </tr>
  </thead>
  <tbody align="center">
    <tr>
      <td>V</td>
      <td>V</td>
      <td>0.8</td>
    </tr>
    <tr>
      <td>V</td>
      <td>F</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td>F</td>
      <td>V</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>F</td>
      <td>F</td>
      <td>0.1</td>
    </tr>
  </tbody>
</table>

Example: the probability of finding a supervisor in a zone, given that there is a machine there but no worker, is 0.2. 

When the robot receives information about a nearby object, it always receives first the object category followed by the object’s name. Example: (you will see these messages in Portuguese): visitante_elsa, zona_montagem, operário_rui. There are different zones in the factory, such as:

 * zone 10 is fixed and is always the factory entrance;
 * assembly, inspection, office, laboratory, packaging and test. In Portuguese
these are called: montagem, inspeção, escritório, laboratório, empacotamento e teste;
 * there may be zones without identification, which can be used for several
tasks.

<!-- Questions -->
### Questions

####  1. Qual foi a penúltima pessoa do sexo masculino que viste?

* [X] **COMPLETED**

#### 2. Em que tipo de zona estás agora?

* [X] **COMPLETED**

#### 3. Qual o caminho para a zona de empacotamento?

* [X] **COMPLETED**

#### 4. Qual a distância até ao laboratório??

* [X] **COMPLETED**

#### 5. Quanto tempo achas que demoras a ir de onde estás até ao escritório?

* [X] **COMPLETED**

#### 6. Quanto tempo achas que falta até ficares sem bateria?

* [X] **COMPLETED** 

#### 7. Qual é a probabilidade da próxima pessoa a encontrares ser um supervisor?

* [X] **COMPLETED**

#### 8. Qual é a probabilidade de encontrar um operário numa zona se estiver lá uma máquina mas não estiver lá um supervisor?

* [X] **COMPLETED**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Members -->
## 🤝 Project Members

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/FuryCode-bit">
        <img src="https://avatars2.githubusercontent.com/u/62396294?s=400&u=7017c42401bedbcc13df785146962b6cd128e658&v=4" width="100px;" alt="Marco 'Fury' Bernardes"/><br>
        <sub>
          <b>Marco Bernardes</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/LucyKirumi">
        <img src="https://avatars.githubusercontent.com/u/130850937?v=4" width="100px;" alt="Pedro Diogo"/><br>
        <sub>
          <b>Lúcia Ferreira</b>
        </sub>
      </a>
    </td>
  </tr>
</table>


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the Apache License 2.0. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/FuryCode-bit/WALL-E-Lost-a-Screw.svg?style=for-the-badge
[contributors-url]: https://github.com/FuryCode-bit/readme-template/graphs/contributors
[license-shield]: https://img.shields.io/github/license/FuryCode-bit/WALL-E-Lost-a-Screw.svg?style=for-the-badge
[license-url]: https://github.com/FuryCode-bit/readme-template/blob/master/LICENSE.txt
[product-screenshot]: readme/fabrica.png